from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from typing import Any, Dict, List, Union
import sys
import io
from rich import print
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from pydantic import BaseModel, validator
from langchain.callbacks.base import AsyncCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
import asyncio
import threading
import queue

console = Console()
# 重定向标准输出
#sys.stdout = custom_output
class ChatResponse(BaseModel):
    """Chat response schema."""

    sender: str
    message: str
    type: str

    @validator("sender")
    def sender_must_be_bot_or_you(cls, v):
        if v not in ["bot", "you"]:
            raise ValueError("sender must be bot or you")
        return v

    @validator("type")
    def validate_message_type(cls, v):
        if v not in ["start", "stream", "end", "error", "info"]:
            raise ValueError("type must be start, stream or end")
        return v

class StreamingRich(StreamingStdOutCallbackHandler):
    
    def __init__(self) -> None:
        super().__init__()
        self.start=True
        self.token_arr=[]
        # 创建一个阻塞队列
        #self.blockingQueues = queue.Queue()
        #self.start_thread()

    def start_thread(self):
        print("start  thread")
        #self.thread=threading.Thread(target=self.start_print_token,args=(self.blockingQueues,))
        # 创建一个阻塞队列
        # 创建并启动工作线程
        #self.thread.daemon=True
        self.thread.start()
    def getText(self):
        MARKDOWN="".join(self.token_arr)
        md = Markdown(MARKDOWN)
        print(md)
        self.blockingQueues.put(md)
        return md
    def start_print_token( self):
        print("start.")
        while self.start:
            with Live(self.getText(),refresh_per_second=4) as live:
                text=self.blockingQueues.get()
                print("live--start")
                live.update(text)
        print("end.")
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
       # self.token_arr.append(token)
        #self.getText()
        sys.stdout.write(token)
        sys.stdout.flush()
        #custom_output.flush()
        #print(token)
        #MARKDOWN="".join(self.token_arr)
        #md = Markdown(MARKDOWN)
        #console.clear_live()
        #console.print(md)
        #sys.stdout.write("123----")
        #custom_output.flush()
        #print("1111-----------------")
        #sys.stdout.write(token)
        #sys.stdout.flush()
        
        #print("".join(self.token_arr))
    def on_text(self, text: str, **kwargs: Any) -> None:
        """Run on arbitrary text."""
        print("text:",text)
    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        print("llm_end---")
        #elf.start=False
        #self.thread.join()


#chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
chat = ChatOpenAI(streaming=True, callbacks=[StreamingRich()], temperature=0)
resp = chat([HumanMessage(content="Scp命令如何上传文件到服务器?")])

