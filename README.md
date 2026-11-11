# workbuddy-push-test

一个用于验证「本地 Git → GitHub 推送」是否打通的最小测试仓库。

## 包含什么

| 文件 | 作用 |
| --- | --- |
| `check_env.py` | 打印当前仓库的 Git 状态（分支、remote、最新提交），在 GitHub 上跑一次即可确认推上去的代码是完整的 |
| `.gitignore` | 忽略 Python 缓存与本地环境文件 |

## 本地验证

```bash
python check_env.py
```

## 推送流程（标准三步）

```bash
git init -b main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/2ECZ/workbuddy-push-test.git
git push -u origin main
```

> 首次推送需要 GitHub 认证。GitHub 自 2021 年起已不接受账号密码，
> 只能用 Personal Access Token（HTTPS）或 SSH 密钥。

## 验证推送成功

```bash
git ls-remote git@github.com:2ECZ/workbuddy-push-test.git
```

能列出 `refs/heads/main` 即表示推送成功。

## 本机连接配置（SSH，免密）

本机已生成 `~/.ssh/id_ed25519_github`（ed25519），公钥登记在 GitHub 账号 `2ECZ` 的
SSH keys 中。`~/.ssh/config` 把 `github.com` 指向 `ssh.github.com:443`（该网络 22 端口不通）：

```bash
git remote set-url origin git@github.com:2ECZ/workbuddy-push-test.git
git push                 # 无需再输入 token
ssh -T git@github.com    # 应返回 Hi 2ECZ!
```

> 私钥不要外传。HTTPS + Personal Access Token 仍然可用，但每次都需要额外传递凭据。
