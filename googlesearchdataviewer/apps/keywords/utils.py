import csv

from django.core.exceptions import ValidationError

from .constants import MAX_KEYWORD_UPLOAD_COUNT


def parse_keyword_csv_file(file):
    reader = csv.reader(file.read().decode('UTF-8').splitlines())

    keyword_count = 0
    parsed_keywords = []
    
    for row in reader:
        if len(row) == 0: continue

        if len(row) > 1:
            raise ValidationError('Invalid CSV format, all keywords should be in a single column', code='invalid')

        keyword_count += 1

        if keyword_count > MAX_KEYWORD_UPLOAD_COUNT:
            raise ValidationError(f'Keywood count reached, maximum {MAX_KEYWORD_UPLOAD_COUNT}', code='invalid')
    
        parsed_keywords.append(row[0])

    if keyword_count == 0:
        raise ValidationError(f'No keywords were uploaded', code='invalid')

    return parsed_keywords