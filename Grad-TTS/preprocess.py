import argparse
import os
from glob import glob
from pathlib import Path

import tgt


def process_utterance(tg_path, basename):
    textgrid = tgt.io.read_textgrid(tg_path)
    phone = get_alignment(
        textgrid.get_tier_by_name("phones")
    )
    text = "{" + " ".join(phone) + "}"

    return "|".join([basename, text])


def get_alignment(self, tier):
    sil_phones = ["sil", "sp", "spn"]

    phones = []
    end_idx = 0
    for t in tier._objects:
        s, e, p = t.start_time, t.end_time, t.text

        # Trim leading silences
        if phones == []:
            if p in sil_phones:
                continue
            else:
                start_time = s

        if p not in sil_phones:
            # For ordinary phones
            phones.append(p)
            end_idx = len(phones)
        else:
            # For silent phones
            phones.append(p)

    # Trim tailing silences
    phones = phones[:end_idx]

    return phones


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--text_grid_folder", type=str, required=False)
    parser.add_argument("--out_filelist", type=str, required=False)
    args = parser.parse_args()

    datasets = []
    for txg in glob(os.path.join(args.text_grid_folder, ".TextGrid")):
        name = Path(txg).stem
        # name = name.split("-")[-1]
        path = os.path.join("DUMMY", f"{name}.wav")
        p = process_utterance(txg, path)
        datasets.append(p)

    split_train = int(len(datasets) * 0.85)
    split_eval = int(len(datasets) * 0.95)
    with open(os.path.join(args.out_filelist, "train.txt"), "w") as fw:
        fw.writelines([f for f in datasets[:split_train]])

    with open(os.path.join(args.out_filelist, "eval.txt"), "w") as fw:
        fw.writelines([f for f in datasets[split_train:split_eval]])

    with open(os.path.join(args.out_filelist, "eval.txt"), "w") as fw:
        fw.writelines([f for f in datasets[split_eval:]])
