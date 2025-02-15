# Beyond Memorization: Assessing Semantic Generalization in Large Language Models Using Phrasal Constructions

This repository contains the data, code and prompts for the paper: Beyond Memorization: Assessing Semantic Generalization in Large Language Models Using Phrasal Constructions.

The experiments can be run using runExperiments.py. The file is annotated with comments and examples to let you know how to customise the code for each experiment.
All the data can be found in the "data" directory. Additionally, the data to run each experiment from the paper is tabulated below.

| Experiment | Setting    | IC Data               | Train Data                                                                   | Test Data                                                                            |
|------------|------------|-----------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 1          | Zero-shot  | None                  | None                                                                         | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 1          | One-shot   | CxNLI                 | constructional_NLI/CxNLI_1_example_train.csv                                 | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 1          | Three-shot | CxNLI                 | constructional_NLI/CxNLI_3_examples_train.csv                                | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 1          | One-shot   | SNLI                  | constructional_NLI/SNLI_1_example_train.csv                                  | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 1          | Three-shot | SNLI                  | constructional_NLI/SNLI_3_examples_train.csv                                 | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 2          | Zero-shot  | None                  | None                                                                         | QA_constructional_reasoning/comparative_correlative_QA_CxReasoning.tsv |
| 2          | Zero-shot  | None                  | None                                                                         | QA_constructional_reasoning/let_alone_QA_CxReasoning.tsv               |
| 2          | Zero-shot  | None                  | None                                                                         | QA_constructional_reasoning/way_manner_QA_CxReasoning.tsv              |
| 3          | Zero-shot  | None                  | None                                                                         | constructional_NLI/CxNLI_3_examples_test.tsv                                         |
| 3          | Zero-shot  | None                  | None                                                                         | abstraction_constructional_NLI/challenge_CxNLI_test.tsv                                |
| 3          | One-shot   | CxNLI                 | constructional_NLI/CxNLI_1_example_train.csv                                 | abstraction_constructional_NLI/challenge_CxNLI_test.tsv                                |
| 3          | Three-shot | CxNLI                 | constructional_NLI/CxNLI_3_examples_train.csv                                | abstraction_constructional_NLI/challenge_CxNLI_test.tsv                                |
| 3          | One-shot   | SNLI                  | constructional_NLI/SNLI_1_example_train.csv                                  | abstraction_constructional_NLI/challenge_CxNLI_test.tsv                                |
| 3          | Three-shot | SNLI                  | constructional_NLI/SNLI_3_examples_train.csv                                 | abstraction_constructional_NLI/challenge_CxNLI_test.tsv                                |

Note: Experiments using o1-preview-2024-09-12 use a subset of each dataset which can be found in the data/o1-preview directory and a temperature of 1, all other models use a temperature of 0.
