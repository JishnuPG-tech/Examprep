# Banking exam domain research

This project uses versioned exam configurations rather than assuming one permanent pattern.

## Official sources reviewed
IBPS CRP PO/MT XVI: https://www.ibps.in/index.php/management-trainees-xvi/
IBPS CRP RRB XV Officer registration: https://ibpsreg.ibps.in/rrbxvaug26/
IBPS recent updates: https://www.ibps.in/index.php/crp-updates/
SBI careers/current openings: https://sbi.co.in/web/careers/current-openings
RBI Assistant Panel Year 2025 recruitment: https://opportunities.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4912

## Design implications
Exam identity must be versioned by organization, exam, cycle/year, stage and section. This prevents one year's pattern from being incorrectly presented as another year's pattern.

Question identity must retain original page, source document hash, extraction method, processing version and validation result.

Current-affairs questions need temporal validity because facts can become stale. The next schema revision should add publication date, event date, validity interval and source reference.

The initial taxonomy separates broad sections from concepts such as inequality, syllogism, seating arrangement, simplification, percentage, data interpretation, reading comprehension and error detection. It should be extended from observed source material and official syllabi.

## Source policy
Only ingest documents the operator is authorized to process. The system preserves provenance and does not include a scraper for protected question-bank sites.
