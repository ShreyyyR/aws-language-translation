import boto3

def en_to_kn_aws(text: str) -> str:
    client = boto3.client("translate", region_name="ap-south-1")
    response = client.translate_text(
        Text=text,
        SourceLanguageCode="en",
        TargetLanguageCode="kn"
    )
    return response["TranslatedText"]

