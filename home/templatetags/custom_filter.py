from django import template
import re
register = template.Library()

@register.filter
def highlight_query(content, query):
    if query:
        # Split the content into parts based on the query
        parts = re.split(f'({re.escape(query)})', content, flags=re.IGNORECASE)
        highlighted_parts = []
        for part in parts:
            if part.lower() == query.lower():
                # Highlight the query part
                highlighted_parts.append(f'<span class="highlight">{part}</span>')
            else:
                highlighted_parts.append(part)
        # Join the parts back together
        return ''.join(highlighted_parts)
    return content