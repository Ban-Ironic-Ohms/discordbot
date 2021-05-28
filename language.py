import language_check

tool = language_check.LanguageTool('en-US')

def checkText(message):
    matches = tool.check(message)
    for mistake in matches:
        return mistake

def numberOfErrors(message):
    matches = tool.check(message)
    return len(matches)