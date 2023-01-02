#!/usr/bin/env python3

import re

dotspcemacs_configuration_layers = """
   ;; ----------------------------------------------------------------
   ;; Example of useful layers you may want to use right away.
   ;; Uncomment some layer names and press `SPC f e R' (Vim style) or
   ;; `M-m f e R' (Emacs style) to install them.
   ;; ----------------------------------------------------------------
   dotspacemacs-configuration-layers
   '(
     protobuf
     auto-completion
     better-defaults
     markdown
     multiple-cursors
     (org :variables
          org-enable-reveal-js-support t
          )
     ivy
     emacs-lisp
     (vimscript :variables
                vimscript-backend 'company-vimscript
                )
     (treemacs :variables
               treemacs-use-all-the-icons-theme t
               treemacs-git-mode 'deferred
               )

     ;; for configuration management
     yaml

     ;; for development environment
     git
     html
     shell-scripts
     (syntax-checking :variables
                      syntax-checking-enable-by-default nil
                      syntax-checking-enable-tooltips nil
                      )
     (cmake :variables
            cmake-backend 'company-cmake
            cmake-enable-cmake-ide-support t
            )
     (c-c++ :variables
            c-c++-enable-google-style t
            c-c++-backend 'lsp-clangd
            c-c++-enable-clang-format-on-save t
            )
     (python :variables
             python-backend 'lsp
             python-formatter 'black
             python-format-on-save t
             python-sort-imports-on-save t
             python-lsp-server 'pyright
             )
     (rust :variables
           rust-format-on-save t)
     (go :variables
         go-backend 'lsp
         go-tab-width 4
         go-format-before-save t
         gofmt-command "goimports")
     (lsp :variables
          lsp-ui-doc-enable nil
          lsp-rust-server 'rust-analyzer
          lsp-enable-file-watchers nil
          )
     (shell :variables
            shell-default-height 30
            shell-default-position 'bottom)
     )
"""


def update_layers(dotspacemacs: str) -> str:
    layers_pattern = re.compile(
        r"(\s*dotspacemacs-configuration-layers\s+'\(\s+.*treemacs\))", re.DOTALL
    )
    dotspacemacs = re.sub(
        layers_pattern, dotspcemacs_configuration_layers, dotspacemacs
    )
    return dotspacemacs


dotspacemacs_themes = """
   dotspacemacs-themes '(
                         monokai
                         doom-one
                         gruvbox-dark-hard
                         spacemacs-dark
                         spacemacs-light
                         leuven
                         )
"""

default_font = """
   dotspacemacs-default-font '("Source Code Pro"
                               :size 12.0
                               :weight normal
                               :width normal)
"""


def update_init(dotspacemacs: str) -> str:
    themes_pattern = re.compile(
        r"\s*dotspacemacs-themes '\(.*spacemacs-light\)", re.DOTALL
    )
    dotspacemacs = re.sub(themes_pattern, dotspacemacs_themes, dotspacemacs)

    font_pattern = re.compile(
        r"\s*dotspacemacs-default-font '\(.*:width normal\)", re.DOTALL
    )
    dotspacemacs = re.sub(font_pattern, default_font, dotspacemacs)

    dotspacemacs = re.sub(
        "dotspacemacs-enable-emacs-pdumper t",
        "dotspacemacs-enable-emacs-pdumper nil",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-editing-style 'vim",
        "dotspacemacs-editing-style 'hybrid",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-elpa-timeout 5", "dotspacemacs-elpa-timeout 15", dotspacemacs
    )
    dotspacemacs = re.sub(
        r"dotspacemacs-mode-line-theme '\(spacemacs :separator wave :separator-scale 1.5\)",
        "dotspacemacs-mode-line-theme '(all-the-icons :separator arrow :separator-scale 1.5)",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-loading-progress-bar t",
        "dotspacemacs-loading-progress-bar nil",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-fullscreen-at-startup nil",
        "dotspacemacs-fullscreen-at-startup t",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-line-numbers nil",
        "dotspacemacs-line-numbers 'relative",
        dotspacemacs,
    )
    dotspacemacs = re.sub(
        "dotspacemacs-smartparens-strict-mode nil",
        "dotspacemacs-smartparens-strict-mode t",
        dotspacemacs,
    )
    return dotspacemacs


user_init = """
(defun dotspacemacs/user-init ()
  "Initialization for user code:
This function is called immediately after `dotspacemacs/init', before layer
configuration.
It is mostly for variables that should be set before packages are loaded.
If you are unsure, try setting them in `dotspacemacs/user-config' first."

  (setq configuration-layer-elpa-archives
        '(
          ("melpa-cn" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")
          ("nongnu" . "https://mirrors.tuna.tsinghua.edu.cn/elpa/nongnu/")
          ("gnu-cn"   . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/")
          ;; ("gnu" . "elpa.gnu.org/packages/")
          ;; ("melpa" . "melpa.org/packages/")
          ;; ("nongnu" . "https://elpa.nongnu.org/nongnu/")
          )
        )
  )
"""


def update_user_init(dotspacemacs: str) -> str:
    user_init_pattern = re.compile(
        r"\(defun dotspacemacs/user-init \(\)\s+.*?\)", re.DOTALL
    )
    dotspacemacs = re.sub(user_init_pattern, user_init, dotspacemacs)
    return dotspacemacs


user_config = """
(defun dotspacemacs/user-config ()
  "Configuration for user code:
This function is called at the very end of Spacemacs startup, after layer
configuration.
Put your configuration code here, except for variables that should be set
before packages are loaded."

  (with-eval-after-load 'org
    ;; for local
    ;; (setq org-re-reveal-root "~/workspace/reveal.js")
    ;; for network
    (setq org-re-reveal-root "https://cdn.jsdelivr.net/npm/reveal.js@3.8.0")
    )


  (setq projectile-project-search-path '("~/workspace"))

  (setq-default evil-escape-delay 0.2)
  (setq-default evil-escape-key-sequence "jk")

  ;; disable Flycheck
  (setq lsp-diagnostics-provider :none)

  )
"""


def update_user_config(dotspacemacs: str) -> str:
    user_config_pattern = re.compile(
        r"\(defun dotspacemacs/user-config \(\)\s+.*?\)", re.DOTALL
    )
    dotspacemacs = re.sub(user_config_pattern, user_config, dotspacemacs)
    return dotspacemacs


def main():
    with open(".spacemacs.template") as f:
        dotspacemacs = "".join(f.readlines())

    dotspacemacs = update_layers(dotspacemacs)
    dotspacemacs = update_init(dotspacemacs)
    dotspacemacs = update_user_init(dotspacemacs)
    dotspacemacs = update_user_config(dotspacemacs)
    print(dotspacemacs)


if __name__ == "__main__":
    main()
