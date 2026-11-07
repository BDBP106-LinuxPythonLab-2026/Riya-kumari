#Class stores a DNA sequence and reports its length,

class DNAsequence:
    def __init__(self,seq): #Things shared in the class are defined here
        self.seq = seq
        self.cleaned_seq="".join(seq.split()).upper()
        self.gc=0
        self.A=0
        self.T=0
        self.G=0
        self.C=0
        self.gc=0
        self.count={}
        self.compliment=""
        self.rev_compliment=""
        self.length = len(self.cleaned_seq)
        self.start_codon="ATG"
        self.codons_translated=[]
        #self.rna=""
        #print("Input sequence",seq)
        #print("Cleaned sequence: ",cleaned_seq)
    def __str__(self):
        return (f'Input sequence:{self.seq} \n'
                f'Cleaned sequence:{self.cleaned_seq}')
    def len(self):

        return self.length
    def basecount(self):
        # self.A =self.cleaned_seq.count("A")
        # self.T = = self.cleaned_seq.count("T")
        # self.G =self.cleaned_seq.count("G")
        # self.C= self.cleaned_seq.count("C")
        # return self.A,self
        #
        # count={}
        #
        # count["A"]=self.cleaned_seq.count("A")
        # count["T"]=self.cleaned_seq.count("T")
        # count["G"]=self.cleaned_seq.count("G")
        # count["C"]=self.cleaned_seq.count("C")

        self.count={base:self.cleaned_seq.count(base) for base in self.cleaned_seq}
        self.A = self.count["A"]
        self.T = self.count["T"]
        self.G = self.count["G"]
        self.C = self.count["C"]
        return self.count

    def gc_content(self):
        self.gc=((self.G+self.C)/self.length*100)
        return self.gc
    def complimentary(self):
        for base in self.cleaned_seq:
            if base=="A":
                self.compliment +="T"
            elif base=="T":
                self.compliment+="A"
            elif base=="G":
                self.compliment+="C"
            elif base=="C":
                self.compliment+="G"
        return self.compliment
    def rev_complimentary(self):
        self.complimentary()
        for i in range(self.length-1,-1,-1):
            self.rev_compliment+=self.compliment[i]
        return self.rev_compliment
    def transcribe(self):
        pairs = {"A":"U","T":"A","G":"C","C":"G"}
        trans=''
        for base in self.cleaned_seq:
            trans+=pairs[base]
        return trans
        # for i in self.cleaned_seq: #we dont need everything to be available to the whole class therefore we don't have to define it globally
        #     if i=="T":
        #         self.rna+="U"
        #     else:
        #         self.rna+=i
        return self.rna
    def find_site(self,seq):
        positions=[]
        start=self.cleaned_seq.find(seq)
        #print(start)
        while start != -1:
            positions.append(start)
            start= self.cleaned_seq.find(seq,start+1)
            #print(start)
        return positions
        #return self.cleaned_seq.count(seq)
    def start(self):
        return self.cleaned_seq.find(self.start_codon)
    def codons(self):
        read_codons=0
        stop_codons=["TAG","TGA","TAA"]
        start_pos=self.start()
        #codons_translated=[]
        for i in range(start_pos,self.length,3):
            code=self.cleaned_seq[i]+self.cleaned_seq[i+1]+self.cleaned_seq[i+2]
            if code in stop_codons:
                break
            read_codons+=1
            self.codons_translated.append(code)
        print("Total codons read :",read_codons)
        return self.codons_translated
    def protein(self):
        dna_codons = {
            # Phenylalanine
            "TTT": "Phenylalanine",
            "TTC": "Phenylalanine",

            # Leucine
            "TTA": "Leucine",
            "TTG": "Leucine",
            "CTT": "Leucine",
            "CTC": "Leucine",
            "CTA": "Leucine",
            "CTG": "Leucine",

            # Isoleucine
            "ATT": "Isoleucine",
            "ATC": "Isoleucine",
            "ATA": "Isoleucine",

            # Methionine (Start codon)
            "ATG": "Methionine",

            # Valine
            "GTT": "Valine",
            "GTC": "Valine",
            "GTA": "Valine",
            "GTG": "Valine",

            # Serine
            "TCT": "Serine",
            "TCC": "Serine",
            "TCA": "Serine",
            "TCG": "Serine",
            "AGT": "Serine",
            "AGC": "Serine",

            # Proline
            "CCT": "Proline",
            "CCC": "Proline",
            "CCA": "Proline",
            "CCG": "Proline",

            # Threonine
            "ACT": "Threonine",
            "ACC": "Threonine",
            "ACA": "Threonine",
            "ACG": "Threonine",

            # Alanine
            "GCT": "Alanine",
            "GCC": "Alanine",
            "GCA": "Alanine",
            "GCG": "Alanine",

            # Tyrosine
            "TAT": "Tyrosine",
            "TAC": "Tyrosine",

            # Stop codons
            # "TAA": "Stop",
            # "TAG": "Stop",
            # "TGA": "Stop",

            # Histidine
            "CAT": "Histidine",
            "CAC": "Histidine",

            # Glutamine
            "CAA": "Glutamine",
            "CAG": "Glutamine",

            # Asparagine
            "AAT": "Asparagine",
            "AAC": "Asparagine",

            # Lysine
            "AAA": "Lysine",
            "AAG": "Lysine",

            # Aspartic acid
            "GAT": "Aspartic acid",
            "GAC": "Aspartic acid",

            # Glutamic acid
            "GAA": "Glutamic acid",
            "GAG": "Glutamic acid",

            # Cysteine
            "TGT": "Cysteine",
            "TGC": "Cysteine",

            # Tryptophan
            "TGG": "Tryptophan",

            # Arginine
            "CGT": "Arginine",
            "CGC": "Arginine",
            "CGA": "Arginine",
            "CGG": "Arginine",
            "AGA": "Arginine",
            "AGG": "Arginine",

            # Glycine
            "GGT": "Glycine",
            "GGC": "Glycine",
            "GGA": "Glycine",
            "GGG": "Glycine"
        }
        self.codons_translated=[]
        codes=self.codons()
        aa_seq=[]
        for code in codes:
            aa_seq.append(dna_codons[code])
        peptide="-".join(aa_seq)
        #print(aa_seq)
        return peptide



#method 1
input_seq="  aactatgAagtgcGgct AAggTTCC Tt"
dna_seq= DNAsequence(input_seq)
print(dna_seq)
print(type(dna_seq))
print("length of the sequence :",dna_seq.len())
print("Base Count :",dna_seq.basecount())
print("GC content :",dna_seq.gc_content())
print("Complimentary DNA :",dna_seq.complimentary())
print("Reverse Complimentary DNA :",dna_seq.rev_complimentary())
print("mRNA :",dna_seq.transcribe())
print("Sites where 'AAG' is present in the seq :",dna_seq.find_site("AAG"))
print("Position of the start codon :",dna_seq.start())
print("Codons translated from the sequence will be :",dna_seq.codons())
print("The peptide formed from the sequence is :",dna_seq.protein())