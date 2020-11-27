from lib.BaseModule import BaseModule
from lib.gui_controls import Controls
import pyautogui
from loguru import logger

# 内功
class NeiGong(BaseModule):

    is_act = True

    def __init__(self):
        logger.info("初始化内功模块")

    def update_hwnd(self,hwnd):
        up = Controls.locate("image\\ng_jxxl.png", hwnd)
        if up:
            pyautogui.leftClick(up)
            logger.info("继续修炼")