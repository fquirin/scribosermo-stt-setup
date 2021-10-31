# Pretrained Scribosermo Checkpoints and Language Models

See: https://gitlab.com/Jaco-Assistant/Scribosermo

## License info given by Scribosermo

By default the checkpoints are provided under the same licence as Scribosermo, but a lot of datasets have extra conditions (for example non-commercial use only) which also have to be applied.
The QuartzNet models are double licenced with [Nvidia's NGC](https://ngc.nvidia.com/catalog/models?query=%20label%3A%22QuartzNet%22) because they use their pretrained weights.  
Please check this yourself for the models you want to use.

## Models

Please download model and scorer files and put them in subfolder "model":

### German

Models
- Quartznet15x5, CV only (WER: 7.5%): [Link](https://www.mediafire.com/folder/rrse5ydtgdpvs/cv-wer0077)
- Quartznet15x5, D37CV (WER: 6.6%):  [Link](https://www.mediafire.com/folder/jh5unptizgzou/d37cv-wer0066)

Scorer: 
- TCV: [Link](https://www.mediafire.com/file/xb2dq2roh8ckawf/kenlm_de_tcv.scorer/file)
- D37CV: [Link](https://www.mediafire.com/file/pzj8prgv2h0c8ue/kenlm_de_all.scorer/file)
- PocoLg: [Link](https://www.mediafire.com/file/b64k0uqv69ehe9p/de_pocolm_large.scorer/file)

### English

Models
- Quartznet5x5 (WER: 4.5%): [Link](https://www.mediafire.com/folder/3c0a353nlppkv/qnet5)
- Quartznet15x5 (WER: 3.7%): [Link](https://www.mediafire.com/folder/eb340s2ab4sv0/qnet15)
- ContextNetSimple (WER: 4.9%): [Link](https://www.mediafire.com/folder/9yess5y8ekvcj/cns8-8b)

Scorer
- [Link](https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer) (to DeepSpeech)
