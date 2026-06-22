from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def redact_pii(text):

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )

    return anonymized_result.text