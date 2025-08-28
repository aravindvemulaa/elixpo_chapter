def build_html_body(token_leaks, commit_hash, diff_info):
        leaks_html = ""
        for leak in token_leaks:
            leaks_html += f"""
            <tr class="border-b">
                <td class="px-4 py-2"><a href="{leak.get('repo_url', '')}" class="text-blue-600 hover:underline">{leak.get('repo_url', '')}</a></td>
                <td class="px-4 py-2"><a href="{leak.get('file_path', '')}" class="text-blue-600 hover:underline">{leak.get('file_path', '')}</a></td>
                <td class="px-4 py-2">{leak.get('line_number', '')}</td>
                <td class="px-4 py-2">{str(leak.get('token', ''))[:8]}...</td>
            </tr>
            """

        html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body class="bg-gray-50 font-sans">
            <div class="max-w-2xl mx-auto my-8 p-6 bg-white rounded shadow">
                <h1 class="text-2xl font-bold text-pink-600 mb-2">🐙 Polli Leaks - Token Exposure Alert</h1>
                <p class="mb-4 text-gray-700">We have detected the following Pollinations token leaks in your repository:</p>
                <table class="min-w-full bg-white border border-gray-200 mb-6">
                    <thead>
                        <tr>
                            <th class="px-4 py-2 bg-gray-100">Repository</th>
                            <th class="px-4 py-2 bg-gray-100">File</th>
                            <th class="px-4 py-2 bg-gray-100">Line</th>
                            <th class="px-4 py-2 bg-gray-100">Token</th>
                        </tr>
                    </thead>
                    <tbody>
                        {leaks_html}
                    </tbody>
                </table>
                <div class="mb-4">
                    <span class="font-semibold text-gray-800">Commit Hash:</span>
                    <span class="font-mono bg-gray-100 px-2 py-1 rounded">{commit_hash}</span>
                </div>
                <div class="mb-4">
                    <span class="font-semibold text-gray-800">Diff Info:</span>
                    <pre class="bg-gray-100 p-2 rounded text-xs overflow-x-auto">{diff_info}</pre>
                </div>
                <p class="text-gray-600 text-sm mt-6">If you have questions, please contact the Polli Leaks team.</p>
            </div>
        </body>
        </html>
        """
        return html

if __name__ == "__main__":
    body = build_html_body(
        token_leaks=[{"repo_url": "https://github.com/example/repo", "file_path": "src/main.py", "line_number": 42, "token": "Poll_XXXX..."}],
        commit_hash="abc123def456",
        diff_info="--- a/src/main.py\n+++ b/src/main.py\n@@ ...\n+Poll_XXXX..."
    )
    print(body)