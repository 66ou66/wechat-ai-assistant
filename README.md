# 微信 AI 自动回复助手

基于 Python + DeepSeek API 的微信 PC 版自动回复工具：持续监控当前聊天窗口的最新消息，调用大模型生成口语化回复并自动发送。

## ⚠️ 免责声明（使用前请务必阅读）

- 本项目**仅供学习研究**，用于学习 Python 自动化、Windows GUI 模拟操作与 LLM API 调用技术，请勿用于任何实际业务或商业用途。
- 程序通过模拟鼠标键盘操作微信客户端实现自动化，**违反微信软件使用协议，存在账号被限制或封禁的风险**。因使用本项目产生的一切后果由使用者自行承担，作者不承担任何责任。
- 请勿利用本项目发送骚扰、广告、诈骗或任何违法违规信息。
- 强烈建议只在小号上测试，不要在主力账号运行。

## 功能特性

- 全自动监控：每 4 秒扫描最近 5 条消息，发现新消息自动回复
- 多消息支持：连发的多条消息按时间顺序逐条回复，同一消息不重复回复
- 上下文对话：保留最近 20 轮对话历史，回复更连贯
- 自定义人设：通过 `character_prompt.txt` 定制语气风格
- 安全防护：Prompt 注入检测、敏感话题拦截、频率限制（冷却 + 小时上限）、脱敏审计日志、剪贴板自动清理

## 环境要求

- Windows + 微信 PC 版
- Python 3.7+

## 安装

```powershell
pip install -r requirements.txt
```

## 配置

1. **API 密钥**：把 `.env.example` 复制一份并重命名为 `.env`，填入你的 DeepSeek API Key（在 [platform.deepseek.com](https://platform.deepseek.com) 注册后创建）：

   ```
   DEEPSEEK_API_KEY=sk-你的密钥
   ```

   `.env` 已被 `.gitignore` 排除，不会被提交到 git。不要把真实密钥写进任何会提交的文件；一旦怀疑泄露，请立即到平台后台作废旧密钥并重新生成。

2. **屏幕坐标**：运行 `获取坐标.py`，把得到的坐标填进 `wechat_ai.py` 顶部的配置区。

3. **角色人设（可选）**：参考 `character_prompt.example.txt` 创建 `character_prompt.txt`。不要在其中写入真实姓名、学校、住址等可识别个人身份的信息；该文件不存在时程序会使用内置的默认人设。

## 运行

双击「启动微信AI助手.bat」，或在终端执行：

```powershell
python wechat_ai.py
```

启动后快捷键：`空格` 开始监控，`1` 暂停/恢复，`Backspace` 退出。监控期间不要移动鼠标或操作键盘，微信窗口保持前台且不最小化。

## 项目结构

```
├── wechat_ai.py                 主程序
├── 获取坐标.py                   屏幕坐标获取工具
├── character_prompt.txt          角色人设（含个人信息，不入库）
├── character_prompt.example.txt  人设模板
├── .env.example                  密钥配置模板
├── requirements.txt              Python 依赖
├── audit.log                     运行审计日志（自动生成，不入库）
└── 启动微信AI助手.bat             一键启动脚本
```
