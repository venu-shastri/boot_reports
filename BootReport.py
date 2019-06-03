import sys
from BootJoiner import joiner
from pather import parse_path

test_results_joins = { 'techsamvit_table_tests_results_answers.csv': {
                                  'index_col': 'id',
                                  'usecols': ['id', 'tests_result_id', 'question_id', 'option_id', 'correct'],
                                  'col_rename': {'id': 'qid'},
                                  'join_with': 'techsamvit_table_tests_results.csv', 'join_on': 'tests_result_id'},
                       'techsamvit_table_tests_results.csv': {'index_col': 'id',
                                  'usecols': ['id', 'test_id', 'user_id', 'test_result'],
                                  'col_rename': None,
                                  'join_with': 'techsamvit_table_users.csv', 'join_on': 'user_id'},
                       'techsamvit_table_users.csv': {'index_col': 'id',
                                  'usecols': ['id', 'name', 'email'],
                                  'col_rename': None,
                                  'join_with': 'techsamvit_table_tests.csv', 'join_on': 'test_id'},
                       'techsamvit_table_tests.csv': {'index_col': 'id',
                                  'usecols': ['id', 'lesson_id', 'title'],
                                  'col_rename': None,
                                  'join_with': 'option-LO.csv', 'join_on': 'option_id'},
                       'option-LO.csv': {'index_col': 'id',
                                  'usecols': ['id', 'option_text', 'suggestion'],
                                  'col_rename': None,
                                  'join_with': None, 'join_on': None}
}

source_directory = parse_path(sys.argv)
test_results = joiner(test_results_joins, source_directory, 'techsamvit_table_tests_results_answers.csv')
outputFilename = 'test_answers_submitted.csv'
test_results.to_csv(outputFilename,
                    columns=['id', 'tests_result_id', 'question_id', 'name', 'email', 'lesson_id', 'suggestion'])
print("Test results written to " + outputFilename)