syntax enable

set backspace=indent,eol,start
let mapleader= ','

"------------------Mappings------------------"
set t_Co=256
colorscheme atom-dark-256

"------------------Mappings------------------"

",ev to edit .vimrc file"
nmap <Leader>ev :tabedit $MYVIMRC<cr>
",ez to edit .zshrc file"
nmap <Leader>ez :tabedit ~/.zshrc<cr>
"Remove Highlighting"
nmap <Leader><space> :nohlsearch<cr>


"------------------Auto-Commands------------------"
set hlsearch
set incsearch

"------------------Auto-Commands------------------"

"Automatically source the vimrc file on save."
augroup autosourcing
        autocmd!
        autocmd BufWritePost .vimrc source %
augroup END
