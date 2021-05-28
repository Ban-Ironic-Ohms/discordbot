import language_check

tool = language_check.LanguageTool('en-US')

def CheckText(message):
    matches = tool.check(message)
    for mistake in matches:
        return mistake

CheckText