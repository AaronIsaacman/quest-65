# Quest 65 Cloud trial

This initial public checkout contains the current cumulative patch, player
guide and static patch-checking tools. The broader local decompilation,
conversation handoffs and infrastructure records are not included yet.

Use a private Codex Cloud environment with access set to **Only me**.
Python 3.10+ and Git are sufficient for this trial. Run:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/cloud_smoke.py --repository-only
```

Supply your own lawful clean US ROM separately as a private task input. The
expected complete-image hash is in `cloud/input-manifest.json`. Do not put the
ROM, input archives, private download URLs or credentials in Git, logs, public
Actions jobs or downloadable public artifacts. The cloud task needs its own
input access before the laptop sleeps; a path on the laptop is insufficient.

Once the private ROM is available, run:

```sh
python3 scripts/cloud_smoke.py --rom /private/path/to/clean-us.z64
```

This checks both complete-image hashes, both N64 checksums and the Test 6
internal build name. It reconstructs Test 6 in memory and writes only a small
JSON report into ignored `build/`. It does not write another ROM, compile
legacy code, execute game instructions or verify played battles. Return the
JSON report and identify whether it was produced locally or in Cloud.

For this trial, make no gameplay changes and do not install IDO, assemblers or
Unicorn. Further game-code execution needs a confirmed isolated remote VM and
the project's network restrictions. Do not weaken a guard to get a test to run.
Do not delegate to additional agents without the user's authorization.

Official setup: [Codex Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments).
