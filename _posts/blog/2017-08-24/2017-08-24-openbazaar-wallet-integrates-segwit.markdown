---
title: "OpenBazaar Wallet Integrates Segwit" 
layout: post
date: '2017-08-24 00:30:00 -0300'
---
        
![](OpenBazaar-Wallet-Integrates-Segwit-1024x512.png)

Segregated Witness has thankfully activated on the Bitcoin network before the release of OpenBazaar 2.0. This has given us an opportunity to upgrade OpenBazaar to make use of segwit before putting it in the hands of users.

Had segwit activated later, it would have made upgrading to segwit much more difficult as all parties to an escrow transaction (the buyer, vendor, and moderator) would need upgrade before segwit could be used. This would also necessitate the need to build in more complex script negotiations to get all parties to agree on what type of script to use. By implementing segwit now we can, hopefully, reduce the fees users will pay to transact on OpenBazaar.

**Specifics**  
For multisig transactions OpenBazaar will use Bech32 encoded pay-to-witness-script-hash (P2WSH) addresses.

![](Segwit-Activated-What-It-Means-for-OpenBazaar.png)

The downside to using this address type is that many external wallets are not yet upgraded to send to these addresses. However, the OpenBazaar internal wallet is, so the worse case scenario if you don’t currently use a segwit compatible wallet is that you can send the coins into the OpenBazaar internal wallet and fund your transaction from there.

For the time being the internal wallet will continue to vend old-style pay-to-pubkey-hash (P2PKH) addresses. We would like to switch to pay-to-witness-pubkey-hash (P2WPKH) addresses but, again, few external wallets support sending to this address type and it would make it difficult for people to send money into the wallet. We could switch to using nested P2SH addresses, but this would be a very disruptive change to our codebase and the benefits aren’t really worth the cost at this point.

Once enough other wallets have enabled sending to P2WPKH we will switch the internal wallet over to P2WPKH. We’ve already done some prep work that will make the transition to the new address type seamless as the wallet will know how to detect payments to and spend from both P2PKH and P2WPKH addresses.

**Escrow with a timeout**  
One related change that we have made but never formally announced is that OpenBazaar2.0 will utilize bip-112 CHECKSEQUENCEVERIFY to add a 45 day (in blocks) timeout to escrow transactions.

One of the big pain points in OpenBazaar v1 was vendors having stuck funds when both a buyer and moderator went unresponsive. By adding a 45 day timeout to the escrow, the vendor will be able to unilaterally move the funds out of escrow and into his wallet after 45 days regardless of whether the buyer and moderator are active or not.

This leaves buyers with 45 days to file a dispute if they have issues with their order (less if they allot time for the dispute resolution process).

**The new scripts look like:**

`OP_IF  
2 <buyer_pubkey><vendor_pubkey><moderator_pubkey> 3 OP_CHECKMULTISIG  
OP_ELSE  
<6480 blocks> OP_CHECKSEQUENCEVERIFY  
OP_DROP  
<vendor_pubkey>  
OP_CHECKSIG  
OP_ENDIF`

If you have any questions or feedback feel free to drop by the [OpenBazaar Slack](http://slack.openbazaar.org/).