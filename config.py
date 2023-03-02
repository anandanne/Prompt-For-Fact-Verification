import argparse


def set_args():
    parser = argparse.ArgumentParser(description='Prompt Tuning For CHEF')
    parser.add_argument('--cuda', type=str, default="0", help='appoint GPU devices')
    # parser.add_argument('--use_cuda', type=bool, default=True, help='if use GPU or not')
    parser.add_argument('--train_file', type=str, default='datasets/claim verification/train.json', help='train dataset path')
    parser.add_argument('--valid_file', type=str, default='datasets/claim verification/dev.json', help='validation dataset path')
    parser.add_argument('--test_file', type=str, default='datasets/claim verification/test.json', help='test dataset path')
    parser.add_argument('--plm', type=str, default='bert', help='bert, bart, T5, gpt')
    parser.add_argument('--num_labels', type=int, default=3, help='num labels of the dataset')
    parser.add_argument('--max_length', type=int, default=512,
                        help='max token length of the sentence for bert tokenizer')
    parser.add_argument('--batch_size', type=int, default=4, help='batch size')
    parser.add_argument('--initial_lr', type=float, default=5e-6, help='initial learning rate')
    parser.add_argument('--initial_eps', type=float, default=1e-8, help='initial adam_epsilon')
    parser.add_argument('--epochs', type=int, default=8, help='training epochs for labeled data')
    parser.add_argument('--freeze', type=bool, default=False, help='freeze plm or not, default is False')
    parser.add_argument('--plm_eval_mode', type=bool, default=False, help='the dropout of the model is turned off')
    parser.add_argument("--template", type=int,
                        help="Set template (0 for manual, 1 for soft, 2 for Ptuning, 3 for PrefixTuning, 4 for PTR, 5 for mix)",
                        default=0)
    parser.add_argument("--verbalizer", type=int,
                        help="Set template (0 for manual, 1 for soft, 2 for knowledge)", default=0)
    return parser.parse_args()