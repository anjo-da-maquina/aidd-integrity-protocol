// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title SuigetsuHoneypot (水月 - Suigetsu Protocol)
 * @dev 囮（おとり）トークンを用いた公金横領トラップ。
 * 監視の目を盗んで不正なアドレスへ資金を流そうとする中間搾取者を検知し、
 * そのウォレットアドレスを永遠にブロックチェーン上に「恥」として刻み込む。
 */
contract SuigetsuHoneypot {
    // 恥の刻印：不正を働いたアドレスを記録するリスト
    mapping(address => bool) public isDisgraced;
    
    // 囮となるトラップ資金の識別用ハッシュ（正規の資金に紛れ込ませる）
    bytes32 private immutable trapTag;

    // 不正発覚時にブロックチェーン全体に通知される永続的なログ
    event DisgraceMarked(address indexed embezzler, string message, uint256 timestamp);
    event TrapTriggered(address indexed from, address indexed to, uint256 amount);

    constructor(bytes32 _trapTag) {
        trapTag = _trapTag;
    }

    /**
     * @notice 資金移動の裏で密かに実行される監視フック
     * @dev 正規の分配処理（ZKP等）をバイパスして、このコントラクトの資金を
     * 動かそうとした瞬間、トラップが発動する。
     */
    function attemptTransfer(address to, uint256 amount, bytes32 tag) external {
        // 対象が罠であることに気づかず、囮資金（trapTag）を動かそうとした場合
        if (tag == trapTag) {
            _triggerSuigetsu(msg.sender, to, amount);
        }
        
        // 正規の資金に見せかけているが、実際には絶対に引き出せない（常にRevert）
        revert("Harakiri: この資金は幻である。");
    }

    /**
     * @notice トラップ発動ロジック。対象を社会的に抹殺する。
     */
    function _triggerSuigetsu(address embezzler, address targetWallet, uint256 amount) internal {
        // 1. 対象のアドレスに「恥」の烙印を押す
        isDisgraced[embezzler] = true;
        isDisgraced[targetWallet] = true;

        // 2. ログの公開（ブロックチェーンの特性上、絶対に消去できない）
        emit TrapTriggered(embezzler, targetWallet, amount);
        emit DisgraceMarked(
            embezzler, 
            "Shame: 公金の横領を検知。このアドレスは不誠実な搾取者として永遠に記録される。", 
            block.timestamp
        );
    }

    /**
     * @notice 外部システムが特定のアドレスの「誉れ」を照会するための関数
     */
    function checkHonor(address target) external view returns (bool hasHonor) {
        return !isDisgraced[target];
    }
}
