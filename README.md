# CustomerSupport Flow

Welcome to the CustomerSupport Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a Flow, leveraging the powerful and flexible framework provided by crewAI.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

You would also need to install
Microsoft C++ 14.x Build Tools:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

Following these instructions for installing and configuring C++ Build Tools:
https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file

Restart PC/Laptop for installation to take effect!!
Add cl to System Path. Its "typically" located at a path which looks something like:
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.34.31933\bin\Hostx86\x86
Verify that cl command works from command line! You can do that by starting Command Prompt and type cl. 
It should give valid version of Microsoft C++ compiler.
```bash
cl
```

Start Command Prompt Termnial inside VS Code.

First, ensure that your now create a Virtual environment so that global python modules do not interfere with this project. And also activate the Virtual environment:
Using Command Prompt:
```bash
python -m venv genai
.\genai\Scripts\activate.bat
```

Now, if you haven't already, install uv:

```bash
pip install uv
```
Its installed either in the .\genai\Scripts folder or in C:\Users\youruserid\.local\bin
Verify that "uv -V" return a valid output. If it does not then PATH variable need to be updated manually.

Run the following command to install crewai CLI:

```bash
uv tool install crewai
```

*** Make sure that the crewai is into your PATH ! Its typically installed in:
C:\Users\youruserid\.local\bin OR in .\genai\Scripts folder

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

This should createa new virtual environment for the project: .\.venv

### Customizing

**Add your `GEMINI_API_KEY` and `MODEL` into the `.env` file**

- Modify `src/customer_support/main.py` to adjust the Flow for Customer Support

## Running the Project

To kickstart your Flow and begin execution, run this from the root folder of your project:

```bash
crewai flow kickoff
```

