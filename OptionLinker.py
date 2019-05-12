import sys
from BootJoiner import joiner
from pather import parse_path

option_question_joins = { 'techsamvit_table_questions_options.csv': {
                                  'index_col': 'id',
                                  'usecols': ['id', 'question_id', 'option_text', 'correct'],
                                  'col_rename': {'id': 'option_id'},
                                  'join_with': 'techsamvit_table_questions.csv', 'join_on': 'question_id'},
                          'techsamvit_table_questions.csv': {'index_col': 'id',
                                  'usecols': ['id', 'question'],
                                  'col_rename': None,
                                  'join_with': None, 'join_on': None}
                        }

source_directory = parse_path(sys.argv)
test_results = joiner(option_question_joins, source_directory, 'techsamvit_table_questions_options.csv')
test_results.to_csv('question-options.csv')
