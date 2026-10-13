# Translation sync preservation

The Traditional Chinese prompt documents are preserved as historical translations, not verified descriptions of current model behavior. Prompt text is repository data only.

During upstream sync, nine generated directory indexes were moved from README.md to INDEX_zh_TW.md in the same directories, without changing their bytes. This preserves upstream README files and avoids case-insensitive collisions with the pre-existing OpenAI/API/readme_zh_TW.md translation. The root Traditional Chinese index and its generator now link/write INDEX_zh_TW.md. The current upstream root README is preserved byte-for-byte with only the Traditional Chinese navigation link added. The lowercase old root readme.md is not recreated.

Historical English prompt files may have moved or been removed upstream; historical index entries and translation text remain unchanged. Use the [pre-sync fork snapshot](https://github.com/jt-ai-tools/system_prompts_leaks/tree/1aa36ddcc249a5d9913d628deaade0a4be98d3aa) to resolve historical originals. No prompts or repository helper scripts were executed.
