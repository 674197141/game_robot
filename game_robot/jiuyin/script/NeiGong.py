from lib.BaseModule import BaseModule
from lib.gui_controls import Controls
from loguru import logger

# 内功
class NeiGong(BaseModule):

    is_act = False

    def __init__(self):
        logger.info("初始化内功模块")

    def update_hwnd(self,hwnd):
        up = Controls.locate("image\\ng_jxxl.png", hwnd,0.8)
        if up:
            Controls.win_mouse_click_box(hwnd,up,True)
            logger.info("继续修炼")