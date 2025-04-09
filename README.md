# CustomerSupport Flow

Welcome to the CustomerSupport Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a Flow, leveraging the powerful and flexible framework provided by crewAI.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `GEMINI_API_KEY` and `MODEL` into the `.env` file**

- Modify `src/customer_support/main.py` to adjust the Flow for Customer Support

## Running the Project

To kickstart your Flow and begin execution, run this from the root folder of your project:

```bash
crewai flow kickoff
```

