For generating candidate Wikipedia entities for entity linking.  

### Requirements
1. The output of the [wikidump_preprocessing](https://github.com/shyamupa/wikidump_preprocessing) generated under the OUTDIR folder, is required for this project. Follow the instructions in that repo for the language of your choice. You also need to prepare the output for the English Wikipedia. 

Make a softlink to the outdir folders generated above under a `data` folder
```bash
$ ln -s path/to/outdir/for/enwiki data/enwiki
```  
where path/to/outdir/for/enwiki is the OUTDIR specified in the makefile of the [wikidump_preprocessing](https://github.com/shyamupa/wikidump_preprocessing) project.

2. pymongo
3. hanziconv

### Setting Up Resources
For faster processing we store the various maps (e.g. string to Wikipedia candidates etc.) in a mongodb database collection. 
To start up the Mongo DB daemon, run: 
```bash
mongod --dbpath /path/to/db/
``` 
The `dbpath` argument is where mongodb will create the database and indexes.  

Once the daemon is running, we can run the candidate generation script. 

### Probability Files
The `CandidateGenerator` class loads Wikipedia matches for a given string, each mapped to the probability of these matches. 

### Title Normalization
The `TitleNormalizer` class is used to resolve ambiguities with multiple titles referring to the same page. These variations of titles appear in redirect pages. A redirect page has no content in itself, but sends the reader to another article in the same wiki. For example, the title `Detective_Sherlock_Holmes` is synonymous with the title `Sherlock_Holmes` and thus redirects to the latter page. 

### Interactive Mode
The interactive mode for candidate generation allows the user to insert a surface form and immediately see the query results in CLI. To run in interactive mode, run: 
```bash
python3 -m wiki_kb.candidate_gen_v2 --lang en --numcands 10 --date 20170520 --interactive
```
Where date is the timestamp of the Wikipedia dump that was processed.
With the interactive flag, the user can enter a surface form as a query string. Here is a example interaction, (user inputs "chicago")

```
enter surface:chicago
cands found: 10
0 Chicago 0.925965 0.0 nrm Chicago phrase
1 Chicago_(band) 0.019539 0.0 nrm Chicago_(band) phrase
2 Chicago_(musical) 0.014488 0.0 nrm Chicago_(musical) phrase
3 Chicago_(2002_film) 0.005084 0.0 nrm Chicago_(2002_film) phrase
4 University_of_Chicago 0.003589 0.0 nrm University_of_Chicago phrase
5 Chicago_Union_Station 0.001794 0.0 nrm Chicago_Union_Station phrase
6 Chicago_Maroons_football 0.001462 0.0 nrm Chicago_Maroons_football phrase
7 Chicago_Blackhawks 0.001379 0.0 nrm Chicago_Blackhawks phrase
8 Chicago_(magazine) 0.001279 0.0 nrm Chicago_(magazine) phrase
9 Chicago_Bears 0.001163 0.0 nrm Chicago_Bears phrase
...
```

### Candidate Generator for Raw Text

TODO
