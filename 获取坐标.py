"""
微信 AI 助手 - 坐标获取工具

使用方法：
  1. 打开微信 PC 版，调整好窗口大小
  2. 运行本脚本
  3. 把鼠标依次移动到以下 3 个位置，记下每次的坐标：

     位置1：聊天列表中「最上面第一个」会话
     位置2：聊天框内「最后一条消息气泡」上
     位置3：底部「输入框」内

  4. 记好后按 Ctrl+C 退出

之后把这些坐标填到「wechat_ai.py」的配置区。
"""

import pyautogui
import time

print("=" * 55)
print("  微信 AI 助手 —— 坐标获取工具")
print("=" * 55)
print()
print("  请把鼠标移动到以下 3 个位置，看到坐标后记下来：")
print()
print("  📌 位置1：聊天列表 - 最上面第一个会话")
print("  📌 位置2：聊天框内 - 最后一条消息气泡上")
print("  📌 位置3：底部输入框内")
print()
print("  ⚠️ 注意：X 坐标通常都一样，约在微信窗口宽度的 40% 处")
print()
print("  按 Ctrl+C 退出")
print("-" * 55)

try:
    while True:
        x, y = pyautogui.position()
        print(f"\r  鼠标坐标：X = {x:4d}  ,  Y = {y:4d}", end="", flush=True)
        time.sleep(0.05)
except KeyboardInterrupt:
    print()
    print()
    print("-" * 55)
    print("  完成！")
    print("  把记下的坐标填到「wechat_ai.py」的配置区：")
    print(f"  CHAT_LIST_X = ?     ← 你的位置1 X")
    print(f"  CHAT_LIST_Y = ?     ← 你的位置1 Y")
    print(f"  MSG_X       = ?     ← 你的位置2 X")
    print(f"  LAST_MSG_Y  = ?     ← 你的位置2 Y")
    print(f"  INPUT_X     = ?     ← 你的位置3 X")
    print(f"  INPUT_BOX_Y = ?     ← 你的位置3 Y")
    print("-" * 55)
