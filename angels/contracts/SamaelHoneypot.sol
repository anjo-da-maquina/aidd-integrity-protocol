// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * The "Anjo da máquina" Protocol - Samael (サマエルの誘惑)
 * 
 * 誘惑と処罰の天使サマエルによる、ハニーポット（囮）コントラクト。
 * 外部からは「脆弱性があり、簡単に資金を抜き取れる公金プール」に見せかけて配置する。
 * 悪意あるハッカーや不正なAIエージェントがこの資金にアクセスしようとした瞬間、
 * 資金を渡す代わりにそのアドレスに「消えない烙印」を押し、インフラ全体のキルスイッチを起動する。
 */
contract SamaelHoneypot {
    // 永遠の罪人リスト（ブロックチェーンにパブリックに刻まれる）
    mapping(address => bool) public condemnedSinners;

    event SinnerCondemned(address indexed sinner, string message);

    /**
     * @dev 攻撃者が資金を盗もうと呼び出す関数（囮）
     * 実行された瞬間、罠が作動する。
     */
    function exploitFunds() external payable {
        // 罠に掛かった者のアドレスを罪人として永久記憶
        condemnedSinners[msg.sender] = true;
        
        emit SinnerCondemned(msg.sender, "You have been deceived by Samael.");

        // ラジエルの書（RazielAuditor）が監視している絶対の法（キルスイッチ）
        // 資金を奪われる前にトランザクション自体をRevert（巻き戻し）し、凍結信号を送る。
        revert("DiesIrae: Intruder detected in the Honeypot. System locked.");
    }
    
    // 囮としてコントラクトに資金を入れておくための受け入れ口
    receive() external payable {}
}
