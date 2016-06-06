# Azure Functions snippets for VS Code

This extension for Visual Studio Code adds snippets for Azure Functions for C# and JavaScript.

## Usage
Type part of a snippet, press `enter`, and the snippet unfolds.

### C\# Snippets
```csharp
azurefunctions-githubwebhook-csharp  // A C# function that will be run whenever it receives a GitHub webhook request
azurefunctions-blobtrigger-csharp // A C# function that will be run whenever a blob is added to a specified container
azurefunctions-eventhubtrigger-csharp // A C# function that will be run whenever an event hub receives a new event
azurefunctions-genericwebhook-csharp // A C# function that will be run whenever it receives a webhook request
azurefunctions-githubcommenter-csharp // A C# function that will be run whenever it receives a GitHub webhook request
azurefunctions-httpget(crud)-csharp // A C# function that fetches entities from a Storage Table when it receives an HTTP request
azurefunctions-httppost(crud)-csharp // A C# function that adds entities to a Storage Table when it receives an HTTP request
azurefunctions-httptrigger-csharp // A C# function that will be run whenever it receives an HTTP request
azurefunctions-imageresizer-csharp // A C# function that creates resized images whenever a blob is added to a specified container
azurefunctions-manualtrigger-csharp // A C# function that is triggered manually via the portal \"Run\" button
azurefunctions-queuetrigger-csharp // A C# function that will be run whenever a message is added to a specified Azure Storage queue
azurefunctions-saasfiletrigger-csharp // A C# function that will be run whenever a file is added to a SaaS provider.
azurefunctions-servicebusqueuetrigger-csharp // A C# function that will be run whenever a message is added to a specified Service Bus queue
azurefunctions-timertrigger-csharp // A C# function that will be run on a specified schedule
```

### JavaScript Snippets
```javascript
githubwebhook-js  // A Node.js function that will be run whenever it receives a GitHub webhook request
```

Alternatively, press `Ctrl`+`Space` (Windows, Linux) or `Cmd`+`Space` (OSX) to activate snippets from within the editor.

## Installation

1. Install Visual Studio Code 0.10.1 or higher
2. Launch Code
3. From the command palette `Ctrl`-`Shift`-`P` (Windows, Linux) or `Cmd`-`Shift`-`P` (OSX)
4. Select `Install Extension`
5. Choose the extension
6. Reload Visual Studio Code