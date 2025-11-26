import os

def simple_markdown_to_html(md_content):
    """
    A very simple markdown to HTML converter.
    Supports:
    - Headings (#, ##, ...)
    - Links ([text](url))
    - Unordered lists (* or -)
    - Paragraphs
    """
    html_lines = []
    in_list = False
    for line in md_content.split('\n'):
        line = line.strip()
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue

        # Headings
        if line.startswith('#'):
            level = len(line.split(' ')[0])
            text = ' '.join(line.split(' ')[1:])
            html_lines.append(f'<h{level}>{text}</h{level}>')
            if in_list:
                html_lines.append('</ul>')
                in_list = False
        # Unordered lists
        elif line.startswith('* ') or line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{line[2:]}</li>')
        # Links on their own line
        elif line.startswith('[') and ']' in line and '(' in line and ')' in line:
             parts = line.split('](')
             text = parts[0][1:]
             url = parts[1][:-1]
             html_lines.append(f'<p><a href="{url}">{text}</a></p>')
             if in_list:
                html_lines.append('</ul>')
                in_list = False
        # Paragraphs
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<p>{line}</p>')

    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

def generate_site():
    """
    Generates a static site from markdown files.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # Find all markdown files in the root directory
    md_files = [f for f in os.listdir('.') if f.endswith('.md')]

    # Read the base template
    with open('templates/base.html', 'r') as f:
        template = f.read()

    # Generate navigation
    nav_links = ''
    for md_file in md_files:
        html_file = os.path.splitext(md_file)[0] + '.html'
        # Use the filename as the link text, and make index the default
        link_text = 'Home' if md_file == 'index.md' else os.path.splitext(md_file)[0]
        nav_links += f'<a href="{html_file}">{link_text}</a>\n'

    # Process each markdown file
    for md_file in md_files:
        with open(md_file, 'r') as f:
            md_content = f.read()

        html_content = simple_markdown_to_html(md_content)

        # Create the final HTML
        final_html = template.replace('{{navbar}}', nav_links)
        final_html = final_html.replace('{{content}}', html_content)

        # Write the HTML file
        html_file = os.path.join('docs', os.path.splitext(md_file)[0] + '.html')
        with open(html_file, 'w') as f:
            f.write(final_html)
        print(f"Generated {html_file}")

if __name__ == '__main__':
    generate_site()