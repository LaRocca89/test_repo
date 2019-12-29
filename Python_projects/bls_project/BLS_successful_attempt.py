exec(open("access_bls_api.py").read())

MD_unemployment = get_series(['OEUN000000000000051000001',
                              'OEUS010000000000051000001',
                              'OEUS020000000000051000001',
                              'OEUS040000000000051000001',
                              'OEUS050000000000051000001',
                              'OEUS060000000000051000001'],
                             2018,
                             2018,
                             'ea1033b94ad643bf98bd7f830fd7cd86')
MD_unemployment.to_csv('50_state_steel_employment.csv')

print(MD_unemployment.head())
