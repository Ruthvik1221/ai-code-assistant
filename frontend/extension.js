const vscode = require('vscode');
const axios = require('axios');

function activate(context) {
    let disposable = vscode.commands.registerCommand('aiCodeAssistant.generateCompletion', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const selection = editor.document.getText(editor.selection);
        if (!selection) {
            vscode.window.showInformationMessage('Select text to generate completion.');
            return;
        }

        const response = await axios.post('http://localhost:8000/generate', { prompt: selection });

        editor.edit(editBuilder => {
            editBuilder.insert(editor.selection.end, "\n" + response.data.completion);
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };
