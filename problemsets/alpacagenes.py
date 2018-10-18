#!/usr/bin/env python3
answer=open("alpacaanswer.txt","w") #create a file to save answers
all_genes=open("alpaca_all_genes.tsv","r")
stem_genes=open("alpaca_stemcellproliferation_genes.tsv","r")
pig_genes=open("alpaca_pigmentation_genes.tsv","r")
gene_set=set()
stem_genes_set=set()
pig_genes_set=set()
for gene in all_genes:
	gene=gene.rstrip()
	gene_set.add(gene)
	gene_set.discard('Gene stable ID')
#print(gene_set)
#if 'Gene stable ID' in gene_set: #this is a good way to check if the element got discarded
#	print("yes")
#else:
#	print("no")
for gene in stem_genes:
	gene=gene.rstrip()
	stem_genes_set.add(gene)
	stem_genes_set.discard('Gene stable ID')
#print(stem_genes)
for gene in pig_genes:
	gene=gene.rstrip()
	pig_genes_set.add(gene)
	pig_genes_set.discard('Gene stable ID')
not_prolif_genes=gene_set.difference(stem_genes_set)#to get no proliferation genes
print(not_prolif_genes)
proli_and_pig_genes=stem_genes_set.union(pig_genes_set)#toget all proliferation and pigmentation genes
print(proli_and_pig_genes)	
#print(pig_genes_set)
#print("all Done")
answer.write(str(proli_and_pig_genes)) #saving in a file

