from masterapp.models import languages_label

def get_label_by_code_and_language(label_code, language='English'):
    try:
        label = languages_label.objects.get(code=label_code)
        if language == 'Arabic':
            return label.arabic
        else:
            return label.english
    except languages_label.DoesNotExist:
        return f'Label with code {label_code} not found'