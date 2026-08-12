# 安装说明

## 通用 Agent Skills 安装

把 `skills/grounded-ai-mentor/` 整个目录复制到客户端的 Skills 目录，保持文件夹名不变。如果客户端只在启动时发现 Skill，请重启，然后先显式测试：

```text
使用 $grounded-ai-mentor，在不预设技术基础的情况下解释 HTTP 请求。
```

## Codex 手动安装

```bash
mkdir -p ~/.codex/skills
cp -R skills/grounded-ai-mentor ~/.codex/skills/grounded-ai-mentor
```

重启 Codex，第一次使用时显式写出 `$grounded-ai-mentor`。

## Codex 插件包

仓库根目录包含 `.codex-plugin/plugin.json`。本地或远程 Marketplace 可以指向这个仓库。由于插件安装界面可能更新，正式发布时应以最新的 Codex 官方插件文档为准。

## 卸载

只删除已经安装的 Skill 文件夹：

```bash
rm -r ~/.codex/skills/grounded-ai-mentor
```

删除前确认路径。项目内 `.grounded-ai-mentor/` 是单独的学习状态，只有学习者明确要求清空时才删除。
