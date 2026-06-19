# Palantir Foundry Ontology 定义与方法论总结

## 一、Ontology 是什么

**Ontology（本体）** 是 Foundry 平台上的**组织运营层（operational layer）**，位于数据集成层（数据集、虚拟表、模型）之上。它将数字资产连接到现实世界的实体——从物理资产（厂房、设备、产品）到概念资产（客户订单、金融交易）。

Ontology 充当组织的**数字孪生（digital twin）**，包含两大类元素：

| 类别 | 元素 | 作用 |
|------|------|------|
| **语义元素** | Object、Property、Link | 描述"是什么"——组织的结构 |
| **动态元素** | Action、Function、Dynamic Security | 描述"做什么"——组织的运营能力 |

---

## 二、核心概念

### 2.1 Object Type / Object / Object Set

这是 Ontology 的基础数据单元，三层结构：

```
Object Type（类型）     ← 定义 schema（类似数据库表定义）
    ↓ 实例化
Object（对象）          ← 单个实体（如员工 "Melissa Chang"）
    ↓ 聚合
Object Set（对象集）    ← 一组对象（如"所有正式员工"）
```

**关键原则：** Object Type 应代表**现实世界的实体**，而非源系统表或技术构件。

```
✗ 避免：MirrorSourceSystemTable（镜像源系统表）
✓ 推荐：Employee、WorkOrder、Vessel（业务语言命名）
```

### 2.2 Property（属性）

Property 是 Object Type 的特征，分为两种：

- **Local Property**：直接在 Object Type 上定义
- **Shared Property**：跨多个 Object Type 共享的标准化属性

Property 应有明确的业务或技术价值，禁止 1:1 映射源系统列（如 `dtLastInspMod` → `lastInspectionDate`）。

### 2.3 Link Type（链接类型）

Link Type 定义两个 Object Type 之间的关系，Link 是该关系的单个实例。

```
Employee ──(Employee → Employer)──→ Company
           ↑                         ↑
        Link Type                  Link 实例
```

**Cardinality（基数）** 决定关系的数量：

| 类型 | 说明 | 示例 |
|------|------|------|
| 1:1 | 一个 Employee 对应一个 Company | 员工 → 雇主公司 |
| 1:N | 一个 Company 对应多个 Employee | 雇主公司 → 员工 |
| N:N | 双向多对多 | Direct Report ↔ Manager（需要 join table） |

Link Type 也支持**自引用**（同一 Object Type 内部的关系）。

### 2.4 Interface（接口）

Interface 描述 Object Type 的**形状（shape）**和**能力**，提供多态性：

```
Interface: Facility
    ├── Property: facilityName, location
    └── 可被实现：
        ├── Airport（实现 Facility + 独有属性）
        ├── Manufacturing Plant（实现 Facility + 独有属性）
        └── Maintenance Hangar（实现 Facility + 独有属性）
```

**Interface vs Object Type：**

| | Object Type | Interface |
|--|------------|-----------|
| 性质 | 具体（concrete） | 抽象（abstract） |
| 实例化 | 可以直接实例化 | 必须通过实现的 Object Type 实例化 |
| 后端数据 | 有 backing datasource | 无 backing datasource |

Interface 支持**继承扩展**（extend），Object Type 可以实现**多个 Interface**。

---

## 三、动态元素（Kinetic Elements）

### 3.1 Action Type（动作类型）

Action 是 Ontology 中**改变数据的交易单位**，Action Type 是可重复执行的编辑定义。

```
Action Type: Assign Employee
    ├── 参数定义：用户输入新角色（表单）
    ├── 业务逻辑：修改 Employee.role property
    ├── 自动行为：在 Employee ↔ Manager 之间创建 Link
    └── 副作用（Side Effects）：通知新旧 Manager
```

Action 的特点：
- **原子性**：一笔交易，失败则回滚
- **可组合**：一次 Action 可修改多个 Object 的多个 Property
- **副作用**：可发送通知、触发 Pipeline 等
- **授权控制**：通过 submission criteria 限制谁能执行

### 3.2 Function（函数）

Function 是在服务器端隔离环境中执行的业务逻辑，支持 TypeScript 和 Python。

**典型用例：**

| 场景 | 说明 |
|------|------|
| Workshop 支持 | 返回 object set 或 variable |
| 派生属性 | function-backed column（派生列） |
| 聚合计算 | Workshop 图表聚合 |
| 复杂编辑 | function-backed action（跨多对象编辑） |
| 外部查询 | external function（查询外部系统丰富 Ontology） |
| Pipeline 集成 | Python function 作为 sidecar 容器 |

---

## 四、Ontology 的支撑体系

### 4.1 Ontology Manager（构建工具）

Ontology Manager（OMA）是构建和维护 Ontology 的主界面，提供以下核心视图：

- **Discover**：收藏/最近查看的 Object Type、Group 浏览
- **Object Type View**：Object Type 的 Overview、Properties、Actions、Link Graph
- **Property Editor**：编辑 Property 定义
- **Link Type View**：配置 Link 的 Cardinality、Key 映射
- **Action Type View**：配置参数、规则、提交条件
- **Function Type View**：Function 的代码编辑

### 4.2 Object Explorer（查询工具）

Object Explorer 是面向非技术用户的**搜索和分析工具**：

- 关键字搜索 + Property 过滤器（点选式，无需 SQL）
- Exploration View（预设可视化：图表、地图）
- 对象集比较与批量 Action
- 跨应用打开（Quiver 等）
- 保存探索结果，实时刷新

### 4.3 安全模型（两层次）

| 层次 | 控制对象 | 说明 |
|------|---------|------|
| **Ontology Resources** | Object Type、Link Type、Action Type 的 Schema | 定义权限（谁可以看/编辑类型定义） |
| **Objects & Links** | 具体的数据行和关系 | 行级安全（谁可以看/编辑哪条数据） |

### 4.4 模型集成（Models）

Ontology 与 Foundry 的模型层（Integrate Models）深度集成：
- Function 可以调用 Language Model
- 模型输出可以作为 Object Property 或 Function 返回值
- 支持 RAG（检索增强生成）模式

---

## 五、设计原则（四大核心原则）

### 原则 1：领域驱动设计（Domain-Driven Design）

> **Ontology 建模的是现实世界，而不是源数据。**

- Object 代表语义上有意义的概念（`Patient`、`WorkOrder`），而非数据库表名
- Link 代表真实关系（"该患者访问过该机构"），而非外键
- 避免 [Kitchen Sink 反模式](#七反模式)：将源系统列 1:1 映射到 Property

### 原则 2：不要重复自己（DRY / Rule of Three）

> **同一语义出现三次，就该重构。**

- 跨团队协作是防止重复的关键
- 使用 Shared Property 避免多处的重复属性定义
- Link Type 的复用优先于新 Link Type 的创建

### 原则 3：开放扩展、封闭修改（Open-Closed Principle）

> **保护核心模型，开放扩展能力。**

- 核心 Object Type 保持稳定
- 通过 Interface 扩展抽象层
- 新业务需求通过新 Object Type / Action 实现，而非修改既有定义

### 原则 4：组合优于深层继承（Composition over Inheritance）

> **用 Interface 多继承替代深层类层次。**

- 避免宽而稀疏的 Object Type（包含大量可选字段）
- 用 Interface 对共享特征建模
- Object Type 可以实现多个 Interface，支持多重多态

---

## 六、开发方法论

### 6.1 Ontology Branching（分支开发）

类似代码分支，Ontology 支持**分支开发**：
- 在分支上开发和测试 Ontology 变更
- 通过 Proposal 提交变更
- 评审通过后合并到主分支

### 6.2 Change Management（变更管理）

所有 Ontology 资源（Object Type、Action Type、Function 等）的变更都通过**变更历史**追踪，支持审计和回滚。

### 6.3 Metadata（元数据管理）

每个 Ontology 资源都有完整的元数据：

| 元数据 | 说明 |
|--------|------|
| **Status** | `active` / `experimental` / `deprecated` |
| **API Name** | 编程时引用的名称 |
| **Display Name** | 用户界面显示的名称 |
| **Visibility** | `prominent` / `normal` / `hidden` |
| **Description** | 业务含义说明 |

---

## 七、反模式（Anti-Patterns）

| 反模式 | 描述 | 正确做法 |
|--------|------|---------|
| **Kitchen Sink** | 一个 Object Type 包含大量无关字段，镜像源系统 | 按领域实体拆分 Object Type |
| **Golden Hammer** | 用 Pipeline 处理本该用 Action 的人工决策 | Action 用于人类决策，Pipeline 用于自动化 |
| **系统镜像** | Object Type 等于源系统表 | 按业务语义建模 |
| **孤岛团队** | 单团队设计 Ontology | 多团队协作，防止重复 |
| **无文档** | 不记录 Object/Property 业务含义 | 在 Ontology Manager 中完整记录 |

---

## 八、典型应用场景

| 场景 | Ontology 如何支持 |
|------|-----------------|
| **运营监控** | Object Explorer 搜索 + Object View 详情 |
| **决策执行** | Action 捕获人工决策（审批、分配、状态变更） |
| **数据写入** | Action 提交 → Writeback Dataset → Pipeline 处理 |
| **跨系统集成** | External Function 查询外部系统，丰富 Object 数据 |
| **AI 辅助运营** | Function 调用 Language Model，Object 作为上下文 |
| **分析协作** | Object Set → Quiver 图表分析 |
| **Workshop 应用** | Workshop 基于 Ontology 构建，无需代码 |

---

## 九、架构总览

```
┌─────────────────────────────────────────────────────────┐
│                    用户应用层                             │
│  Object Explorer │ Workshop │ Quiver │ Slate │ SDK      │
├─────────────────────────────────────────────────────────┤
│                   Ontology 层                            │
│  ┌──────────────┬───────────────┬────────────────┐      │
│  │   语义元素   │   动态元素    │   接口元素      │      │
│  │ Object Type  │ Action Type  │   Interface    │      │
│  │  Property   │  Function    │               │      │
│  │  Link Type  │              │               │      │
│  └──────────────┴───────────────┴────────────────┘      │
│                        ↓                                 │
│  ┌──────────────────────────────────────────────┐        │
│  │            Ontology Manager（构建工具）        │        │
│  └──────────────────────────────────────────────┘        │
│                        ↓                                 │
├─────────────────────────────────────────────────────────┤
│                   数据集成层                             │
│  Dataset │ Virtual Table │ Model (AI/ML)                 │
└─────────────────────────────────────────────────────────┘
```

---

## 十、快速参考

**创建顺序建议：**

```
1. 定义 Object Type（语义基础）
   → 确定有哪些现实世界实体

2. 定义 Property（Object 的特征）
   → 标准化命名，业务语言

3. 定义 Link Type（实体间关系）
   → 确定 Cardinality 和 Key

4. 定义 Interface（如有抽象需求）
   → 提取公共形状

5. 定义 Action Type（运营行为）
   → 捕获决策和写入逻辑

6. 定义 Function（如需复杂逻辑）
   → 派生计算、外部集成
```

**关键约束：**
- Link 不支持跨不同 Ontology
- Object Type 必须有 backing datasource 才能实例化
- Action 是原子事务，包含完整逻辑和副作用
- Interface 不直接实例化，必须通过实现的 Object Type 访问
