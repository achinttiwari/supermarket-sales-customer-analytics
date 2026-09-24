# Development

## Checks

```bash
ruff check .
pytest
streamlit run app.py
```

## Principles

- Keep transformations in src/.
- Keep Streamlit focused on presentation and interaction.
- Never commit raw customer transaction data.
- Never fabricate findings when the source CSV is unavailable.
- Add tests when changing cleaning, RFM, or model behavior.
