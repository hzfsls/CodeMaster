import spacy
from tqdm import tqdm
import random

if __name__ == "__main__":
    # Load English tokenizer, tagger, parser and NER
    spacy.prefer_gpu()
    nlp = spacy.load("en_core_web_trf")

    code_file = "data/target-dataset/train.code"
    comment_file = "data/target-dataset/train.comment"

    output_code_file = "data/target-dataset-NP/train.code"
    output_before_part_file = "data/target-dataset-NP/train.before"
    output_after_part_file = "data/target-dataset-NP/train.after"
    output_target_file = "data/target-dataset-NP/train.target"

    codes = []
    comments = []
    output_codes = []
    output_bps = []
    output_tgts = []
    output_aps = []

    with open(code_file, encoding="utf-8") as f:
        for codeline in f:
            code = codeline.strip()
            codes.append(code)
    with open(comment_file, encoding="utf-8") as f:
        for commentline in f:
            comment = commentline.strip()
            comments.append(comment)

    # codes = codes[:1000]
    # comments = comments[:1000]

    # Process whole documents
    for idx, comment in enumerate(tqdm(comments)):
        doc = nlp(comment)
        for chunk in doc.noun_chunks:  # 提取所有名词区区块
            if len(chunk.text.split(' ')) <= 1:  # 名词短语长度为 1则删去
                continue
            start_i = chunk.start
            end_i = chunk.end
            # # 划分为前中后三段
            # before_part = doc[:start_i]
            # target = doc[start_i:end_i]
            # after_part = doc[end_i:]

            before_part_tokens = []
            target_tokens = []
            after_part_tokens = []

            for token in doc:
                if token.i < start_i:
                    before_part_tokens.append(token.text)
                elif start_i <= token.i < end_i:
                    target_tokens.append(token.text)
                else:
                    after_part_tokens.append(token.text)

            before_part = ' '.join(before_part_tokens)
            target_tokens = ' '.join(target_tokens)
            after_part = ' '.join(after_part_tokens)
            output_codes.append(codes[idx])
            output_bps.append(before_part)
            output_tgts.append(target_tokens)
            output_aps.append(after_part)

    with open(output_code_file, 'w', encoding='utf-8') as f:
        for c in output_codes:
            f.write(c + '\n')
    with open(output_before_part_file, 'w', encoding='utf-8') as f:
        for c in output_bps:
            f.write(c + '\n')
    with open(output_target_file, 'w', encoding='utf-8') as f:
        for c in output_tgts:
            f.write(c + '\n')
    with open(output_after_part_file, 'w', encoding='utf-8') as f:
        for c in output_aps:
            f.write(c + '\n')
