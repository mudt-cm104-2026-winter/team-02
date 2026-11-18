# Cybersecurity Study Resources

<!-- Replace the title with your project name. -->

## What this is 
Personal library of cybersecurity learning resources. You enter the URL of website you studied from, assign it to a cybersecurity topic, and the app saves it and shows the full list of URLs grouped by topic.

<!-- One or two sentences: what does your app do, and who is it for?
Right now it is the example "Things to bring". Replace it with your topic. -->

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in resources.json and remain available after restarting the application.

## Team
<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->


| GitHub | Role |
|---|---|
| dkolacnikov | python |
| judyahmadd | HTML and CSS |
| urosuros25 | Documentation |



## How we work
- Although the work is divided into three areas, everyone helps everyone in all parts of the project. Every change goes through its own branch and pull request, and each pull request needs the approval of at least one other team member before it is merged. We start every work as an issue and track it on our project board. 

- Donat was in charge of programming the app in python and made sure that the repository looked clean all the times. The issues and sub-issues were created and taken care of by him. With every pull request at least one issue was closed, and he was the person in team that secured it.

- Uros created documentation successfully by constantly being in contact with both team members, understanding the reason behind every change in code and pull request. It was his responsibility to create a merge conflict on purpose and solve it without any further problems.

- Judy was responsible for developing CSS and HTML file. He made sure that the design on the web page looks simple and straight-forward. All the features our site has are there thanks to him.

- In conclusion, we tried doing our best for this project. The project made us learn Github and its powerful features: how to state a problem, how to solve it in team and which way to capture and save our solution. As a team, we crave next challenges this subject has to offer. No one went for the beers.(during the project, though celebrated with one after completing it)

<!-- How your team uses Git. For example:
- one branch per issue, named after it: `12-add-glossary`
- every pull request needs one approval from another team member
- the author merges after the approval
- every pull request adds a line to CHANGELOG.md
-->

## Sources 

No Sources were used for doing this project. 

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI 

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
- 2026-11-13/15: Claude, used for making and improving the python program, code checked before every run 
- 2026-11-15/16: Chatgpt, used for making the app's latest version of CSS and HTML file, checked by running the app in the browser
- 2026-11-16: Claude, used for making template for documentation file README.md and to correct punctuality, checked by all team members
- 2026-11-16: ChatGPT, used in Python and HTML integration

