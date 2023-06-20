import logging 
import os 
from datetime import datetime

Log_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Log_File) ##it will add in cwd
os.makedirs(logs_path,exist_ok=True) #eventhoug there is file keep appending it

Log_File_PATH=os.path.join(logs_path,Log_File)

logging.basicConfig(
    filename=Log_File_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
)