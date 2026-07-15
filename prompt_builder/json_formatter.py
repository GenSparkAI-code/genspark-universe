import json


class JsonFormatter:

    def format(self, text: str) -> str:

        if not text.strip():
            return ""

        try:
            data = json.loads(text)
        except Exception:
            return text

        return self._format_dict(data)

    def _format_dict(
        self,
        data,
        indent=0,
    ):

        lines = []

        prefix = "  " * indent

        if isinstance(data, dict):

            for key, value in data.items():

                key = key.replace("_", " ").title()

                if isinstance(value, (dict, list)):

                    lines.append(
                        f"{prefix}{key}:"
                    )

                    lines.append(
                        self._format_dict(
                            value,
                            indent + 1,
                        )
                    )

                else:

                    lines.append(
                        f"{prefix}{key}: {value}"
                    )

        elif isinstance(data, list):

            for item in data:

                if isinstance(
                    item,
                    (dict, list),
                ):

                    lines.append(
                        self._format_dict(
                            item,
                            indent,
                        )
                    )

                else:

                    lines.append(
                        f"{prefix}- {item}"
                    )

        return "\n".join(lines)