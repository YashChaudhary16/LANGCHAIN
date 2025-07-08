# LangChain Agents Workflow Diagram

## Overview
This diagram shows the complete workflow executed in `agents.ipynb`, demonstrating how to build a tool-calling agent with Wikipedia and ArXiv search capabilities.

## Workflow Flowchart

```mermaid
graph TD
    A[Start: Install Dependencies] --> B[Setup Tools]
    B --> C[Setup LLM & Agent]
    C --> D[Execute Agent Queries]
    D --> E[End]

    %% Dependencies Installation
    A --> A1[Install wikipedia package]
    A --> A2[Install arxiv package]
    A --> A3[Install langchainhub package]

    %% Tool Setup
    B --> B1[Wikipedia Tool Setup]
    B --> B2[ArXiv Tool Setup]
    B --> B3[Tool Collection]

    B1 --> B1a[Import WikipediaQueryRun]
    B1 --> B1b[Create WikipediaAPIWrapper]
    B1 --> B1c[Configure: top_k_results=1, doc_content_chars_max=200]
    B1 --> B1d[Create wiki_tool]

    B2 --> B2a[Import ArxivQueryRun]
    B2 --> B2b[Create ArxivAPIWrapper]
    B2 --> B2c[Configure: top_k_results=1, doc_content_chars_max=200]
    B2 --> B2d[Create arxiv_tool]

    B3 --> B3a[Combine tools: [wiki_tool, arxiv_tool]]

    %% LLM & Agent Setup
    C --> C1[Environment Setup]
    C --> C2[LLM Configuration]
    C --> C3[Prompt Template]
    C --> C4[Agent Creation]
    C --> C5[Agent Executor]

    C1 --> C1a[Load .env file]
    C1 --> C1b[Set ANTHROPIC_API_KEY]

    C2 --> C2a[Import ChatAnthropic]
    C2 --> C2b[Create LLM: claude-3-5-sonnet-20240620]
    C2 --> C2c[Set temperature=0]

    C3 --> C3a[Create ChatPromptTemplate]
    C3 --> C3b[Define system message]
    C3 --> C3c[Add user input placeholder]
    C3 --> C3d[Add agent_scratchpad placeholder]

    C4 --> C4a[Import create_tool_calling_agent]
    C4 --> C4b[Create agent with LLM, tools, prompt]

    C5 --> C5a[Import AgentExecutor]
    C5 --> C5b[Create executor with agent, tools]
    C5 --> C5c[Set verbose=True]

    %% Query Execution Examples
    D --> D1[Query 1: Tesla CEO]
    D --> D2[Query 2: BranchyNet Authors]
    D --> D3[Query 3: BranchyNet Research Papers]

    %% Query 1 Flow
    D1 --> D1a[Input: "Who is the CEO of Tesla?"]
    D1a --> D1b[Agent decides to use Wikipedia tool]
    D1b --> D1c[Search: "Tesla CEO"]
    D1c --> D1d[Result: Tesla, Inc. page]
    D1d --> D1e[Agent refines search: "Elon Musk Tesla CEO"]
    D1e --> D1f[Result: Wealth of Elon Musk page]
    D1f --> D1g[Agent searches: "Tesla company leadership"]
    D1g --> D1h[Final response: Elon Musk is CEO since 2008]

    %% Query 2 Flow
    D2 --> D2a[Input: "Who are the authors of BranchyNet paper?"]
    D2a --> D2b[Agent decides to use ArXiv tool]
    D2b --> D2c[Search: "BranchyNet: Fast Inference via Early Exiting from Deep Neural Networks"]
    D2c --> D2d[Result: Different paper found]
    D2d --> D2e[Agent refines search with quotes]
    D2e --> D2f[Result: Correct paper found]
    D2f --> D2g[Final response: Surat Teerapittayanon, Bradley McDanel, H. T. Kung]

    %% Query 3 Flow
    D3 --> D3a[Input: "How many research papers are based on BranchyNet?"]
    D3a --> D3b[Agent uses ArXiv tool]
    D3b --> D3c[Search: "BranchyNet"]
    D3c --> D3d[Result: Original paper found]
    D3d --> D3e[Agent searches with OR operator]
    D3e --> D3f[Result: Still only original paper]
    D3f --> D3g[Final response: Limitations explained, suggests broader search needed]

    %% Styling
    classDef setup fill:#e1f5fe
    classDef tool fill:#f3e5f5
    classDef agent fill:#e8f5e8
    classDef query fill:#fff3e0
    classDef decision fill:#ffebee

    class A,A1,A2,A3 setup
    class B,B1,B2,B3,B1a,B1b,B1c,B1d,B2a,B2b,B2c,B2d,B3a tool
    class C,C1,C2,C3,C4,C5,C1a,C1b,C2a,C2b,C2c,C3a,C3b,C3c,C3d,C4a,C4b,C5a,C5b,C5c agent
    class D,D1,D2,D3,D1a,D1b,D1c,D1d,D1e,D1f,D1g,D1h,D2a,D2b,D2c,D2d,D2e,D2f,D2g,D3a,D3b,D3c,D3d,D3e,D3f,D3g query
    class D1b,D2b,D3b decision
```

## Detailed Process Flow

### Phase 1: Setup & Dependencies
1. **Package Installation**
   - Install `wikipedia` for Wikipedia API access
   - Install `arxiv` for ArXiv paper search
   - Install `langchainhub` for prompt templates

### Phase 2: Tool Configuration
1. **Wikipedia Tool**
   - Create `WikipediaAPIWrapper` with limited results (top_k=1, max_chars=200)
   - Wrap in `WikipediaQueryRun` tool
   
2. **ArXiv Tool**
   - Create `ArxivAPIWrapper` with same limitations
   - Wrap in `ArxivQueryRun` tool
   
3. **Tool Collection**
   - Combine tools into list: `[wiki_tool, arxiv_tool]`

### Phase 3: Agent Setup
1. **Environment & LLM**
   - Load environment variables
   - Initialize Claude 3.5 Sonnet with temperature=0
   
2. **Prompt Engineering**
   - Create system message for tool selection
   - Add user input and agent scratchpad placeholders
   
3. **Agent Assembly**
   - Create tool-calling agent with LLM, tools, and prompt
   - Wrap in AgentExecutor with verbose logging

### Phase 4: Query Execution Examples

#### Example 1: Tesla CEO Query
```
Input → Agent Reasoning → Wikipedia Tool → Refined Search → Final Answer
```

#### Example 2: BranchyNet Authors Query
```
Input → Agent Reasoning → ArXiv Tool → Refined Search → Final Answer
```

#### Example 3: BranchyNet Research Papers Query
```
Input → Agent Reasoning → ArXiv Tool → Multiple Searches → Limitations Explanation
```

## Key Features Demonstrated

1. **Tool Selection**: Agent automatically chooses appropriate tool (Wikipedia vs ArXiv)
2. **Iterative Refinement**: Agent refines search queries when initial results are insufficient
3. **Error Handling**: Agent explains limitations when tools can't provide complete answers
4. **Verbose Logging**: Full transparency of agent's reasoning process
5. **Function Calling**: Demonstrates Claude's ability to call external tools

## Technical Architecture

```
User Query → Agent Executor → Tool-Calling Agent → LLM (Claude 3.5 Sonnet)
                                    ↓
                            Tool Selection Logic
                                    ↓
                    [Wikipedia Tool] [ArXiv Tool]
                                    ↓
                            External APIs
                                    ↓
                            Formatted Response
```

This workflow demonstrates a complete LangChain agent system with external tool integration, showing how AI agents can leverage multiple data sources to answer complex queries. 