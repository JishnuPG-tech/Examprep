# Banking Examination Domain Specification

Version: 2026.1
Purpose: domain contract for the Examprep document/question extraction pipeline.

## 1. Scope

Primary recruitment families:
- IBPS PO/MT
- IBPS Customer Service Associate (CSA)
- IBPS RRB Office Assistant
- IBPS RRB Officer Scale I
- IBPS RRB Officer Scale II General Banking Officer
- IBPS RRB Officer Scale II Specialist Cadres
- IBPS RRB Officer Scale III
- IBPS Specialist Officer: IT, Agriculture Field Officer, Law, HR/Personnel, Marketing, Rajbhasha
- SBI Probationary Officer
- SBI Junior Associate
- RBI Assistant
- RBI Grade B

## 2. Extraction principle

Official exam schema and question taxonomy are different layers.

Official schema comes from the current notification/information handout:
organization, exam, cycle, post, stage, paper/test, section, question count, marks, time, negative marking, language, sectional timing, qualifying/merit status.

Question taxonomy is granular classification from actual questions:
subject/section, topic, subtopic, micro-topic, question format, reasoning operation, mathematical skill, grammar rule, knowledge domain, difficulty, data representation, dependency structure and answer type.

Never replace the official schema with a generic syllabus list.

## 3. Current exam-pattern matrix

### IBPS PO/MT
Current 2026 CRP PO/MT-XVI reference.

Preliminary:
- English Language: 30 questions, 30 marks, 20 min
- Quantitative Aptitude: 35 questions, 30 marks, 20 min
- Reasoning Ability: 35 questions, 40 marks, 20 min
- Total: 100 questions, 100 marks, 60 min
- Separately timed sections

Main, 2026 XVI:
- Reasoning: 40 questions, 60 marks, 45 min
- General/Economy/Banking Awareness including Digital/Financial Awareness and RBI circulars: 50 questions, 60 marks, 35 min
- English Language: 40 questions, 20 marks, 35 min
- Data Analysis & Interpretation: 40 questions, 60 marks, 45 min
- Objective: 170 questions, 200 marks, 160 min
- Descriptive: 2 tasks, 25 marks, 30 min
- Current cycle includes essay and comprehension.

The 2026 pattern differs from the preceding PO cycle. Pattern must therefore be stored by cycle.

### IBPS CSA
Current CSA family.

Preliminary:
- English Language: 30 / 30 / 20 min
- Numerical Ability: 35 / 35 / 20 min
- Reasoning Ability: 35 / 35 / 20 min
- Total 100 / 100 / 60 min

Main:
- General/Financial Awareness: 40 / 50 / 20 min
- General English: 40 / 40 / 35 min
- Reasoning Ability: 40 / 60 / 35 min
- Quantitative Aptitude: 35 / 50 / 30 min
- Total 155 / 200 / 120 min

Use the exact cycle notification as final source of truth.

### IBPS RRB Office Assistant
Preliminary:
- Reasoning: 40 / 40 / 25 min
- Numerical Ability: 40 / 40 / 20 min
- Total 80 / 80 / 45 min

Main:
- Reasoning: 40 / 50 / 30 min
- Computer Knowledge: 40 / 20 / 15 min
- General Awareness: 40 / 40 / 15 min
- English OR Hindi: 40 / 40 / 30 min
- Numerical Ability: 40 / 50 / 30 min
- Total 200 / 200 / 120 min

Language choice and state-specific language availability must be stored.

### IBPS RRB Officer Scale I
Preliminary:
- Reasoning: 40 / 40 / 25 min
- Quantitative Aptitude: 40 / 40 / 20 min
- Total 80 / 80 / 45 min

Main:
- Reasoning: 40 / 50 / 30 min
- Computer Knowledge: 40 / 20 / 15 min
- General Awareness: 40 / 40 / 15 min
- English OR Hindi: 40 / 40 / 30 min
- Quantitative Aptitude: 40 / 50 / 30 min
- Total 200 / 200 / 120 min

### IBPS RRB Officer Scale II/III
These are separate from the Scale-I pattern.

Scale-II General Banking Officer:
- Reasoning
- Computer Knowledge
- Financial Awareness
- English/Hindi Language
- Quantitative Aptitude & Data Interpretation

Scale-II Specialist Cadre adds Professional Knowledge and has a different allocation.

Scale-III:
- Reasoning
- Computer Knowledge
- Financial Awareness
- English/Hindi Language
- Quantitative Aptitude & Data Interpretation

Use the cycle-specific notification for exact allocations.

### SBI PO
Preliminary:
- English Language: 30 / 30
- Quantitative Aptitude: 35 / 35
- Reasoning Ability: 35 / 35
- Total 100 / 100 / 1 hour

Main objective:
- Reasoning & Computer Aptitude: 45 / 60 / 60 min
- Data Analysis & Interpretation: 35 / 60 / 45 min
- General Awareness about Economy/Banking: 40 / 40 / 35 min
- English Language: 35 / 40 / 40 min
- Total 155 / 200 / 3 hours

Descriptive:
- English Language: 50 marks / 30 min
- Letter Writing and Essay

Phase III:
- Group Exercise
- Interview

### SBI Junior Associate
Preliminary:
- English Language: 30 / 30 / 20 min
- Quantitative/Numerical Ability: 35 / 35 / 20 min
- Reasoning Ability: 35 / 35 / 20 min
- Total 100 / 100 / 60 min

Main:
- General/Financial Awareness: 50 / 50 / 35 min
- General English: 40 / 40 / 35 min
- Quantitative Aptitude: 50 / 50 / 45 min
- Reasoning Ability & Computer Aptitude: 50 / 60 / 45 min
- Total 190 questions / 200 marks / 2 h 40 min

Local-language testing can apply.

### RBI Assistant
Current Panel Year 2025:
Preliminary:
- English Language: 30 / 30 / 20 min
- Numerical Ability: 35 / 35 / 20 min
- Reasoning Ability: 35 / 35 / 20 min
- Total 100 / 100 / 60 min

Main:
- Reasoning: 40 / 40 / 30 min
- English: 40 / 40 / 30 min
- Numerical Ability: 40 / 40 / 30 min
- General Awareness: 40 / 40 / 25 min
- Computer Knowledge: 40 / 40 / 20 min
- Total 200 / 200 / 135 min

Then Language Proficiency Test for applicable office/state language.

### RBI Grade B
Maintain separate schemas for Phase I, Phase II, General, DEPR and DSIM.

General includes:
- General Awareness
- Reasoning
- English Language
- Quantitative Aptitude

Phase II General includes:
- Economic and Social Issues
- Finance and Management
- English Writing Skills

Do not merge RBI Grade B into the PO/Clerk taxonomy.

### IBPS Specialist Officer
Post-specific:
- IT Officer
- Agricultural Field Officer
- Law Officer
- HR/Personnel Officer
- Marketing Officer
- Rajbhasha Adhikari

Prelims differ by post family. Mains require professional-knowledge taxonomies.

Professional examples:
IT: DBMS, networking, operating systems, data structures, programming/OOP, software engineering, computer organization, cybersecurity, banking IT.
AFO: crop production, agronomy, soil, horticulture, seed science, irrigation, animal husbandry, agricultural economics, agroforestry, ecology, agriculture schemes, agricultural finance.
Marketing: marketing management, consumer behaviour, segmentation, product, price, promotion, distribution, branding, sales, retail, market research, service marketing, digital marketing, CSR, business ethics.

Other specialist cadres require dedicated controlled vocabularies.

## 4. Quantitative Aptitude taxonomy

Arithmetic:
- percentage: increase/decrease, successive percentage, population, expenditure/income, marks, election/votes, composition
- ratio/proportion: direct, inverse, compound ratio, partnership
- average: simple, weighted, replacement, age
- profit/loss: CP, SP, MP, discount, successive discount
- simple interest
- compound interest: annual, half-yearly, quarterly, growth/depreciation
- time/work: efficiency, work equivalence, pipes/cisterns
- time/speed/distance: relative speed, trains, boats/streams, races
- mixtures/alligation
- partnership
- ages
- probability
- permutation/combination

Number/algebra:
- simplification
- approximation
- number system
- divisibility
- HCF/LCM
- remainders
- fractions/decimals
- surds/indices
- quadratic equations
- equations
- number series: missing, wrong, double-pattern, arithmetic, geometric, alternating

Mensuration:
- 2D perimeter/area
- 3D surface area/volume

Data Analysis/DI:
- table
- bar graph
- line graph
- pie chart
- caselet
- missing DI
- arithmetic DI
- percentage DI
- ratio DI
- average DI
- mixed graph
- radar/web graph
- data sufficiency
- quantity comparison
- data comparison
- probability-based DI
- permutation/combination-based DI

Store data representation separately from mathematical topic.

## 5. Reasoning taxonomy

Arrangement:
- linear seating
- circular seating
- square/rectangular seating
- parallel rows
- floor/flat
- box
- shelf
- scheduling
- day/month/year
- ranking/order
- comparison
- grouping/distribution

Logical/analytical:
- syllogism
- inequality
- coding-decoding
- blood relation
- direction sense
- alphanumeric series
- number/letter series
- input-output
- data sufficiency
- statement-conclusion
- statement-assumption
- statement-argument
- cause-effect
- course of action
- inference
- decision making

Puzzle metadata:
- number of entities
- entity types
- dimensions
- number of conditions
- fixed positions
- relative conditions
- negative conditions
- conditional conditions
- either/or conditions
- possibility conditions
- uniqueness constraints
- question dependency graph

## 6. English taxonomy

Reading:
- reading comprehension
- factual
- inference
- vocabulary-in-context
- tone
- title/main idea
- statement-based
- passage completion

Grammar:
- subject-verb agreement
- tenses
- articles
- prepositions
- conjunctions
- pronouns
- adjectives/adverbs
- modifiers
- parallelism
- conditionals
- voice
- narration
- sentence structure
- punctuation

Objective:
- error detection
- sentence correction
- phrase replacement
- fillers
- double fillers
- cloze test
- para jumbles
- sentence rearrangement
- word swap
- odd sentence
- connector
- word usage
- vocabulary
- synonyms
- antonyms
- idioms/phrases

Descriptive:
- essay
- letter
- report
- email
- precis/summary
- comprehension

## 7. General/Banking/Financial Awareness

Banking:
- RBI
- monetary policy
- repo/reverse repo
- CRR
- SLR
- bank rate
- MSF
- liquidity
- banking regulation
- payment systems
- digital banking
- financial inclusion
- priority sector lending
- NPA
- provisioning
- Basel norms
- capital adequacy
- banking institutions
- committees
- banking terminology

Financial markets:
- money market
- capital market
- equity
- debt
- bonds
- treasury bills
- commercial paper
- certificates of deposit
- mutual funds
- insurance
- pensions
- derivatives
- forex
- exchange rates

Economy:
- GDP
- GNP
- inflation
- unemployment
- fiscal policy
- monetary policy
- balance of payments
- exchange rate
- national income
- taxation
- government budget
- economic surveys
- development indicators

Government schemes should store:
scheme name, ministry, launch year, target group, objective, funding, eligibility, benefit, current status, source date.

Current affairs should store:
event date, publication date, valid_from, valid_until if applicable, organization/person/entity, geography, category, source and fact version.

Never treat current affairs as timeless facts.

## 8. Computer Awareness

- hardware
- CPU
- memory
- storage
- input/output devices
- operating systems
- file systems
- software
- programming basics
- DBMS
- networking
- internet
- protocols
- web
- cloud
- cybersecurity
- malware
- encryption
- authentication
- digital signatures
- MS Office
- shortcuts
- databases
- AI/ML basics
- digital payments
- banking technology

## 9. Question formats

Identify:
- MCQ
- multiple-select
- true/false
- assertion-reason
- statement-based
- match-the-following
- fill-in-the-blank
- numeric answer
- descriptive
- essay
- letter
- case study
- puzzle multi-question set
- DI set
- RC set
- cloze set

## 10. Question dependency

A source may contain one common context followed by multiple questions.

Store:
- set_id
- parent_context
- child_question_id
- dependency_type

Examples:
RC passage -> questions
puzzle -> questions
DI table -> questions
cloze passage -> questions

Never destroy the common context when splitting questions.

## 11. Difficulty

Do not let an LLM arbitrarily assign difficulty.

Store independent signals:
- calculation length
- logical constraint count
- inference steps
- vocabulary rarity
- distractor similarity
- data volume
- number of operations
- time pressure
- ambiguity
- concept depth

Suggested labels:
very_easy, easy, moderate, difficult, very_difficult.

Keep difficulty_source and difficulty_model_version.

## 12. Answer model

Separate:
- answer_key
- answer_text
- accepted_answers
- explanation
- source_answer
- verified_answer
- verification_status

Verification states:
- source_confirmed
- independently_verified
- conflicting
- missing
- review_required

Never overwrite the original source answer when independent verification disagrees.

## 13. Provenance

Every extracted field should be traceable.

Required:
- source_document_id
- source_sha256
- page_number
- block_id
- character offsets where available
- extraction_method
- extractor_version
- model/provider/model_version if model-assisted
- timestamp
- confidence

Generated explanations should additionally store:
- generated_by
- generation_version
- evidence references
- verification state

## 14. Source-document types

Classify:
- official notification
- official information handout
- official mock/test material
- official syllabus
- question paper
- memory-based paper
- answer key
- solution PDF
- coaching material
- current-affairs PDF
- book/chapter
- user-created material

Authority hierarchy:
1. current official notification
2. current official information handout
3. official recruitment material
4. official institutional source
5. independently sourced question paper
6. memory-based reconstruction
7. coaching material
8. user-created/generated material

Authority level must travel with every extracted fact/question.

## 15. Confidence

Keep separate:
- OCR confidence
- segmentation confidence
- question extraction confidence
- answer extraction confidence
- classification confidence
- verification confidence
- overall confidence

Do not collapse all uncertainty into one internal score.

## 16. Exam-version identity

Recommended key:
organization + exam_code + post + cycle + stage + paper + section

Example:
IBPS | PO_MT | PO | XVI | MAIN | OBJECTIVE | REASONING

Never use only IBPS PO as identity.

## 17. Official research sources

- IBPS PO/MT XVI: https://www.ibps.in/index.php/management-trainees-xvi/
- IBPS RRB XV: https://www.ibps.in/index.php/rural-bank-xv/
- IBPS CSA XVI: https://www.ibps.in/index.php/clerical-cadre-xvi/
- IBPS SPL XVI: https://www.ibps.in/index.php/specialist-officers-xvi/
- SBI PO: https://sbi.co.in/web/careers/probationary-officers
- SBI Junior Associate: https://sbi.co.in/web/careers/junior-associate
- RBI Assistant Panel Year 2025: https://opportunities.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4912

Recheck these sources whenever a new cycle is added.

## 18. Implementation requirement

The database/configuration layer should represent this specification as data, not parser conditionals.

For each document/question, the pipeline should determine:
1. exam version
2. stage/paper
3. section
4. document type
5. question/set type
6. topic/subtopic
7. evidence supporting the answer
8. confidence
9. authority
10. verification state

This specification is the domain contract for extraction workers.
