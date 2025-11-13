import os
from setuptools import setup, find_packages
from distutils.sysconfig import get_config_vars

from torch.utils.cpp_extension import BuildExtension, CUDAExtension

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

version = os.environ.get("SPTR_VERSION", "1.0.0")

setup(
    name='sptr',
    version=version,
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('sptr_cuda', [
            'src/sptr/pointops_api.cpp',
            'src/sptr/attention/attention_cuda.cpp',
            'src/sptr/attention/attention_cuda_kernel.cu',
            'src/sptr/precompute/precompute.cpp',
            'src/sptr/precompute/precompute_cuda_kernel.cu',
            'src/sptr/rpe/relative_pos_encoding_cuda.cpp',
            'src/sptr/rpe/relative_pos_encoding_cuda_kernel.cu',
            ],
        extra_compile_args={'cxx': ['-g', '-O3'], 'nvcc': ['-O3']}
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    python_requires='>=3.8',
)
