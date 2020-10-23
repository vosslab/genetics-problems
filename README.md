# genetics-problems
Python Scripts for Generating Genetics Homework/Quiz problems

[comment]: <> ( https://guides.github.com/features/mastering-markdown/ )
[comment]: <> ( https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes )
[comment]: <> ( https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax )

Table of Contents
=================

   * [genetics-problems](#genetics-problems)
      * [Blood Types](#blood-types)
         * [blood_type_offspring.py](#blood_type_offspringpy)
         * [blood_type_mother.py](#blood_type_motherpy)
         * [hla_genotype.py](#hla_genotypepy)
      * [Gametes](#gametes)
         * [gametes_unique.py](#gametes_uniquepy)
      * [Epistasis](#epistasis)
         * [epistasis_test_cross.py](#epistasis_test_crosspy)
         * [epistasis_inverse_test_cross.py](#epistasis_inverse_test_crosspy)


## Blood Types

### blood_type_offspring.py

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-blood_type_offspring.txt)

1. For the ABO blood group in humans, the i<sup>A</sup> and i<sup>B</sup> alleles are codominant and the i allele is recessive. If a female &female; with <u>type A blood</u> marries a male &male; with <u>type O blood</u>, which of the following blood types could their children possibly have? Check all that apply.

- [x] A. Type O blood
- [x] B. Type A blood
- [ ] C. Type B blood
- [ ] D. Type AB blood

### blood_type_mother.py

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-blood_type_mother.txt)

2. For the ABO blood group in humans, the i<sup>A</sup> and i<sup>B</sup> alleles are codominant and the i allele is recessive. A father &male; who has <u>blood type AB</u> has a son &male; who has <u>blood type A</u>, which of the following blood types could the mother &female; possibly have? Check all that apply.

- [x] A. Type O blood
- [x] B. Type A blood
- [x] C. Type B blood
- [x] D. Type AB blood
- [ ] E. None of the above are possible

### hla_genotype.py

* [Download list of 2 gene questions in blackboard upload format](blackboard_upload/bbq-hla_genotypes-2_genes.txt)
* [Download list of 3 gene questions in blackboard upload format](blackboard_upload/bbq-hla_genotypes-3_genes.txt)

3. A mother has a HLA genotype of A2,B5,C6 on one chromosome and A1,B1,C3 on the other. The father has a HLA genotype of A7,B9,C2 on one chromosome and A8,B3,C5 on the other. Which one of the following is a possible genotype for one of their offspring?
- [ ] A. A2,A8,B1,B9,C2,C3
- [ ] B. A1,A2,B1,B5,C3,C6
- [x] C. A2,A7,B5,B9,C2,C6
- [ ] D. A7,A8,B3,B9,C2,C5
- [ ] E. A1,A7,B1,B3,C5,C6

## Gametes

### gametes_unique.py 

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-gametes_unique.txt)

1. How many unique gametes could be produced through independent assortment by an individual with the genotype AA Bb cc dd Ee Ff Gg ?
- [ ] A. 2<sup>2</sup> = 4
- [ ] B. 2<sup>3</sup> = 8
- [x] C. 2<sup>4</sup> = 16
- [ ] D. 2<sup>5</sup> = 32
- [ ] E. 2<sup>6</sup> = 64


## Epistasis

### epistasis_test_cross.py

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-epistasis_test_cross.txt)

1. In a specific cross, F<sub>2</sub> progeny exhibit a modified dihybrid ratio of <b>15:1</b> (instead of 9:3:3:1 ). What phenotypic ratio would be expected from a test-cross with an individual from the F<sub>1</sub> progeny?
- [ ] A. 1:4
- [ ] B. 2:2 or 1:1
- [ ] C. 4:1
- [x] D. 3:1
- [ ] E. 2:1
- [ ] F. 1:3

### epistasis_inverse_test_cross.py

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-epistasis_inverse_test_cross.txt)

2. An F<sub>1</sub> heterozygote individual from dihybrid cross is used for a test-cross. The progeny from the test-cross exhibited a modified <b>ratio of 3:1</b> (instead of 1:1:1:1). What phenotypic ratio would be expected in the F<sub>2</sub> progeny if the dihybrid cross is continued?
- [x] A. 13:3
- [ ] B. 12:4
- [ ] C. 11:5
- [ ] D. 10:6
- [ ] E. 9:7

## X-linked disorders

### poisson_flies.py

* [Download list of questions in blackboard upload format](blackboard_upload/bbq-poisson_flies.txt)


<p>1. The white-eyed phenotype is an X-linked recessive disorder in fruit flies. The red allele, +, is dominant to the white allele, w. The offspring of size 400 from the mating of a single female and a single male are shown in the table below:</p>

<table cellpadding="2" cellspacing="2" style="border-collapse: collapse; text-align:center; border: 1px solid black; font-size: 14px;"><tr><th>phenotype</th><th>female &female;</th><th>male &male;</th></tr> <tr><td>red-eyed (wildtype)</td><td align='center'>0</td><td align='center'>0</td></tr> <tr><td>white-eyed (mutant)</td><td align='center'>185</td><td align='center'>215</td></tr> </table>

<p><strong>What are the genotypes of the parents in this cross?</strong></p>

- [ ] A. homozygous wildtype female (++) and male of unknown genotype
- [ ] B. heterozygous female (+w) and wildtype male (+&ndash;)
- [ ] C. heterozygous female (+w) and mutant male (w&ndash;)
- [ ] D. homozygous mutant female (ww) and wildtype male (+&ndash;)
- [x] E. homozygous mutant female (ww) and mutant male (w&ndash;)

