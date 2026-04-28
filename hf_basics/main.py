from transformers import pipeline

#  first time run this code it download this model 4 GB model 

pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages)