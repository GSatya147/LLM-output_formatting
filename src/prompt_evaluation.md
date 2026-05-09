### prompt evaluation core steps:
1. Output quality comparison
2. Hallucination rate
3. Format accuracy

## HAMEL INTUITION:
For successful evals we need fast iterating systems on these:
1. Evaluating quality (eg: tests)
2. Debugging issues (eg: logging and inspecting data)
3. Changing the behaviour of system (prompt engg, fine-tuning and writing code)

#### The types of Evaluations we can adopt (depending on cost ascending order): 
Level 1: Unit Tests
Level 2: Model & Human Eval (this includes debugging)
Level 3: A/B testing

**Level 1: Unit tests**
    - Just like assertions we write in pytests can be achieved through 3 steps
    step 1: Write scoped test - assertions
    Step 2: Create Test cases (edge too) - can automate using LLMs
    step 3: Run and track - can be done through github actions (CI/CD)

**Level 2: Human & Model evals**
    - After basic assertions to move towards step we need some prequisites:
    1. Logging traces - can use LangSmith 
    2. Looking at your traces - labelling good or bad/ using custom built tools to diagnose
    3. Automated evals using LLMs - generally more powerful LLM judging our LLM responses

**Level 3: A/B Testing** Industry standard for mature products
    - Comparing two different states/versions of our model, distinction is based on user behaviour

**Evaluating RAGs** 
- Aside from evaluating our system as a whole, we  can evaluate sub-components of our AI like RAGs.
"""