# hashed-cron

---

## Description
Hashed-cron is a library that aim to create a better scheduler in your jobs, minimizing parallel execution in your compute resources.

This library is inspired in Jenkins Hash syntax.
According to it's documentation:

> To allow periodically scheduled tasks to produce even load on the system, the symbol H (for “hash”) should be used wherever possible. For example, using 0 0 * * * for a dozen daily jobs will cause a large spike at midnight. In contrast, using H H * * * would still execute each job once a day, but not all at the same time, better using limited resources. The H symbol can be used with a range. For example, H H(0–7) * * * means some time between 12:00 AM (midnight) to 7:59 AM. You can also use step intervals with H, with or without ranges. The H symbol can be thought of as a random value over a range, but it actually is a hash of the job name, not a random function, so that the value remains stable for any given project. 

Source: https://www.jenkins.io/doc/book/pipeline/syntax/

A blog post: https://medium.com/@dev.thiago/minimize-scheduled-concurrency-with-hashed-cron-library-25433c7760c4


---

## Installation

```shell
pip install hashed-cron
```

---
## Usage

```python
from hashed_cron import cron_converter

cron = "H H * * *"

converted_cron = cron_converter.convert(cron, "job_01")

print(converted_cron)

# Result: 41 5 * * *
```



---
## Examples 

| Hashed Cron | Identifier | Result     |
|-------------|------------|------------|
| H * * * * | job_01     | 41 * * * * |
| H H * * *   | job_01   | 41 5 * * *       |
| H * * * *  | job_02   | 16 * * * *       |
| H H * * *   | job_02   | 16 4 * * *       |
| H/30 * * * *   | job_02   | 16/30 * * * *       |
| H/10 H/3 * * *   | job_02   | 6/10 1/3 * * *       |
| H/10 H/3 0/2 * *   | job_02   | 6/10 1/3 0/2 * *       |


---
## Bugs

If you find any bug, please add an issue on https://github.com/thiagowig/hashed-cron/issues