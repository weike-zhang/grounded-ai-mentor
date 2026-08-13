# 安装说明

## 推荐：Agent Skills CLI

下面的公网命令要等远程仓库得到授权并改名为 `grounded-ai-tutor` 后才会生效。在此之前请从当前本地检出安装。

```bash
npx skills add weike-zhang/grounded-ai-tutor \
  --skill grounded-ai-tutor -g
```

如果客户端只在启动时发现 Skill，请重启，然后测试：

```text
使用 $grounded-ai-tutor，在不预设技术基础的情况下解释 HTTP 请求。
```

更新或卸载：

```bash
npx skills update grounded-ai-tutor -g
npx skills remove grounded-ai-tutor -g
```

## Codex 手动安装

克隆仓库，只复制可安装的 Skill 文件夹：

```bash
git clone https://github.com/weike-zhang/grounded-ai-tutor.git
mkdir -p ~/.codex/skills
cp -R grounded-ai-tutor/skills/grounded-ai-tutor \
  ~/.codex/skills/grounded-ai-tutor
```

重启 Codex，第一次使用时显式写出 `$grounded-ai-tutor`。

## 校验本地仓库

在仓库根目录运行：

```bash
python -m unittest discover -s tests -v
python evals/validate_fixtures.py
```

测试覆盖学习状态的授权和敏感信息语义；夹具命令验证发布结构。两者都不给模型行为评分，也不代表已经获得持久化或分享学习状态的授权。

## 手动卸载

如果之前是手动复制，先核对路径，再只删除已经安装的 Skill 文件夹：

```bash
rm -r ~/.codex/skills/grounded-ai-tutor
```

项目中的学习状态目录与 Skill 安装目录相互独立。只有学习者明确要求清空时才删除学习状态。
