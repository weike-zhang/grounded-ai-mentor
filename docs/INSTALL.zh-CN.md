# 安装说明

## 推荐：Agent Skills CLI

```bash
npx skills add weike-zhang/grounded-ai-mentor \
  --skill grounded-ai-mentor -g
```

如果客户端只在启动时发现 Skill，请重启，然后测试：

```text
使用 $grounded-ai-mentor，在不预设技术基础的情况下解释 HTTP 请求。
```

更新或卸载：

```bash
npx skills update grounded-ai-mentor -g
npx skills remove grounded-ai-mentor -g
```

## Codex 手动安装

克隆仓库，只复制可安装的 Skill 文件夹：

```bash
git clone https://github.com/weike-zhang/grounded-ai-mentor.git
mkdir -p ~/.codex/skills
cp -R grounded-ai-mentor/skills/grounded-ai-mentor \
  ~/.codex/skills/grounded-ai-mentor
```

重启 Codex，第一次使用时显式写出 `$grounded-ai-mentor`。

## 校验本地仓库

在仓库根目录运行：

```bash
python evals/validate_fixtures.py
```

它只验证夹具结构和发布文件，不给模型行为评分。

## 手动卸载

如果之前是手动复制，先核对路径，再只删除已经安装的 Skill 文件夹：

```bash
rm -r ~/.codex/skills/grounded-ai-mentor
```

项目中的学习状态目录与 Skill 安装目录相互独立。只有学习者明确要求清空时才删除学习状态。
