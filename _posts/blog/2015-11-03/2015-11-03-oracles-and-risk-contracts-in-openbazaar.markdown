---
title: "Oracles and Risk Contracts in OpenBazaar" 
layout: post
date: '2015-11-03 00:30:00 -0300'
---
        
[![1-oWCGi1RYfyMAbKpobLkolA](1-oWCGi1RYfyMAbKpobLkolA.png)](https://blog.openbazaar.org/wp-content/uploads/2015/10/1-oWCGi1RYfyMAbKpobLkolA.png)

OpenBazaar is, among other things, a contracting platform that enables two or more parties to trade any _thing._ But if there is a common theme to the last few articles we have published, it is that the applications don’t stop at traditional e-commerce.

One application of particular interest is the formation of speculative contracts that depend on the unknown future _state_ of an object or event.

Speculative contracts are a fundamental component of the market economy. They form the basis of insurance policies, loans, and futures markets just to name a few.

Typically, enforcement of speculative contracts are handled through the courts or trusted third parties that have exclusive control of funds. With Bitcoin and Ricardian contracts, speculative contracts can be resolved directly between two parties, or in cooperation with a mutually selected third party in the event of a dispute.

To achieve this in OpenBazaar, we need to define a new user role on the network, an _Oracle,_ who will report on the _state_ of an object or event in the future. Secondly, we will need a Ricardian contract schema for various types of speculative contracts, which we will refer to as **risk contracts**.

This article will review the role of _Oracles_ in OpenBazaar and how risk contracts will be settled on the platform.

Oracles
-------

**Oracles** are nodes on the OpenBazaar network that report on the _state_ of any object or event in the future. Based on the Oracle’s report, a **risk contract** is settled in favor of the user who correctly predicted the future _state_.

In OpenBazaar, the responsibilities of an Oracle will depend on the individual user. In short, they can either serve as a:

1.  Reporter
2.  Escrow agent (i.e. Moderator)

As a **reporter**, the _Oracle_ can publicly report on the _state_ of an object or event over time, which will serve as a data input for risk contracts between other users. These users may have little or no interaction with the Oracle directly, who can serve _state_ reports in plain-text publicly or via OpenBazaar’s instant messaging service. _Oracles_ may even report the _state_ of an object or event using their own sophisticated APIs similar to [Reality Keys](https://www.realitykeys.com/). Critically, **reporter**_Oracles_ do not handle any user funds and are not Moderators.

_Oracles_ can also serve as the escrow agent or **Moderators**, where the future_state_ of the object or event, which they report on, is the basis of releasing funds from multisignature escrow to the appropriate party. Releasing funds would be done in cooperation with the winning party. This service may only be necessary if the losing party is a _sore loser_, refusing to release funds for immature reasons. Ideally, _Oracles_ would only be required to release funds in the event of a dispute.

Just as with Moderators, an open market for _Oracles_ introduces competitive forces and diversity to improve the quality and range of data sources. _Oracles_can advertise what categories of objects or events they will report on, and why they are uniquely qualified over their peers. The _Oracle’s_ reputation system will reflect how accurately they report _state_ and citing reputable sources.

Any user can become an _Oracle_.

Risk Contracts
--------------

**Risk contracts** are a class of Ricardian contract that settle the transfer of funds to a party based on the future _state_ of an object or event. There are four types of risk contracts that OpenBazaar will support:

1.  **Lending and Bonds** (peer-to-peer loans, debt securities)
2.  **Insurance** (dispute insurance, traditional consumer/business insurance)
3.  **Forward and Futures** (asset price speculation)
4.  **Prediction/Information** (object or event state speculation)

For nearly all of these classes of risk contracts, an Oracle is required to validate the state of an object or event. In some contracts, the Moderator will act as the Oracle.

The **risk contract** schema is comparable to that of typical e-commerce Ricardian contracts in OpenBazaar. As a quick refresher, every _listing contract_has the following objects that are filled with data:

1.  **Metadata** object — related to the type of contract and version of the contract
2.  **ID of the Vendor** object — e.g. GUID, blockchain ID (if stated), public keys
3.  **Market** object — semantic properties of the _thing_ being sold
4.  **Policy** object— Terms and conditions, returns (if relevant)
5.  **Moderator** object— ID and public keys of the Moderator

All of the above objects are signed with the Vendor’s GUID to complete the listing contract that is published to the network.

In e-commerce contracts, the **market object** describes the physical/digital good or the type of service the user will perform. For example, this is the market object for a physical item:

"item" : {
    "title" : "",
    "description" : "",
    "condition" : "",
    "price\_per\_unit" : {
       "bitcoin" : "",
       "fiat" : {
          "price" : "",
          "currency_code" : ""
       }
    },
    "item_properties" : "",
    "quantity" : "",
    "category" : \[ "" \],
    "image_hashes" : \[ "" \],
    "keywords" : \[ "" \],
    "process_time" : "",
    "sku" : ""
}

The **market object** will list specific contract details depending on the type of risk contract it is (e.g. loans: principal, interest, term; insurance: policy T&Cs, premiums, excess etc). The reference market object, which captures the details for all types of risk contracts, is:

"**risk**" : {
   "type" : "",                **// Risk contract type**
   "description" : "",         **// Description of loan, policy, etc**
   "loan" : {                  **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "loan_repayments" : {
      "interest\_rate\_pa": 0,   **// % per annum**
      "interest_calc": "",     **// Daily, monthly, year**
      "repayments_sched": "",  **// Repayment schedule**
      "bitcoin" : "",          **// Denominated in bitcoin or fiat**
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "loan_collateral" : {       **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "insurance_type" : "",      **// Full, partial, zero-limit**
   "policy_limit" : {          **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "insurance_reserve" : 0,    **// % collateral to be kept in escrow**
   "insurance_coverage" : "",  **// What the policy covers**
   "insurance_premium" : {     
      "type" : "",             **// One-off or regular**
      "schedule" : "",         **// Payment frequency**
      "bitcoin" : "",          **// Denominated in bitcoin or fiat**
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "insurance_excess" : {      **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "futures_asset" : "",       **// Name of the asset**
   "limit\_per\_unit": {         **// Max up/down exposure**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "prediction_state" : "",    **// Future state of object/event**
   "units" : "",               **// Quantity of asset/shares** **purchased**
   "price\_per\_unit" : {        **// Future price; bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "position" : "",            **// Short, long**
   "term_days": "",            **// Term of the contract**
   "oracle_source" : "",       **// Oracle user ID + sources**
   "keywords": \[\]              **// Enhanced search**
}

For each type of risk contract discussed below, we will examine the schema of the **market** **object** and briefly touch on the mechanics of the trade flow.

### Lending and Bonds

_Peer-to-peer loans_ and _bonds_ can be offered in OpenBazaar using the following **market object**:

"**risk**" : {
   "type" : "loan",
   "description" : "",         **// Description of the loan**
   "loan_repayments" : {
      "interest\_rate\_pa": 0,   **// % per annum**
      "interest_calc": "",     **// Daily, monthly, year**
      "repayments_sched": "",  **// Repayment schedule**
      "bitcoin" : "",          **// Denominated in bitcoin or fiat**
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "term": "",                 **// Term of the loan**
   "loan_collateral" : {       **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "keywords": \[\]
}

For this type of contract, the Moderator acts as the _Oracle_, as the repayments are made to the Lender from the Buyer in bitcoin. The role of the _Oracle_ in this scenario is to regulate the release of _collateral_ (i.e. a reserve requirement) from the multisignature escrow address once the loan is repaid **or** the borrower has defaulted.

In terms of discovery, the borrower may place an _invitation to tender_ for a loan, where the above listing contract is a tender proposal. Creditors can submit their _loan offers_ to the borrower, who sorts through the competing offers to select one with the best terms.

This approach would give creditors a great deal of flexibility to tailor and compete on parameters such as the interest rate, reserve requirement, term, and repayment schedule **based** on the _reputation_ of the borrower. Indeed, the creditor may require higher interest rates and collateral for pseudonymous users with a limited or poor reputation, relative to pseudonymous users with a high reputation or users with several public endpoints connected to their Blockchain ID.

An alternate approach is for the creditor to offer standardized loans (i.e. bonds) on the network. Other users can purchase these bonds from the creditor, receiving interest repayments as per a normal bond. As this market matures, users will buy and sell bonds as a typical financial asset on the OpenBazaar network.

Unlike physical or digital goods, or services, the _trade flow_ is more straightforward after the loan is approved/bond purchased. Bitcoin repayments on principal and interest payments are made to addresses specified in the contract ([stage 3 of the trade flow](https://blog.openbazaar.org/decentralized-reputation-in-openbazaar/)).

The OpenBazaar application will keep track of repayments and manage dispute resolution through the Moderator as per normal.

### Insurance

_Insurance contracts_ in OpenBazaar can be offered in one of three forms:

1.  Fully collateralized
2.  Partially collateralized
3.  No limit

A **fully collateralized** insurance contract would lock the entire value of the policy (i.e. the maximum coverage limit) in multisignature escrow, while the policyholder pays regular premiums to the insurer.

Theoretically, the accrued premiums plus collateral would be equal to the policy limit, but this may place the insurer at a financial disadvantage given that the policy funds are locked and are not yielding any interest.

However, if there is no claim on the policy, the insurer will collect premiums that can be loosely considered a _financial_ coupon that yields the insurer a reward for risking funds up-front for the policyholder. The _pseudo_ coupon rate may be higher than low-yield government bonds, but significantly more risky. This may also turn insurance policies in OpenBazaar into tradeable financial instruments.

Premiums for this type of insurance contract may be higher than standard policies, and may even exceed the policy limit. However, in exchange for the higher premiums, the policyholder is secure in the knowledge that if the policy is triggered, all of the funds are accessible.

Unlike partially collateralized insurance contracts, there is **zero chance** **of the insurer defaulting** due to an inability to pay the policy limit, at the cost of the policyholder. This represents a significant technological advance in the insurance industry.

A **partially collateralized** insurance contract only locks a percentage of the policy’s value in multisignature escrow throughout the life of the policy.

As the full limit of the insurance policy is no longer locked in a multisignature escrow, the policyholder is now trusting the insurer to transfer the necessary amount of funds in the event of a claim. There is a risk of the insurer defaulting, which may be caused by financial mismanagement, higher than expected frequency/severity of claims, or simply fraud. A combination of regulation, reinsurance contracts, and transparent proof of reserves could potentially be used to mitigate the risk of the insurer defaulting.

Partially collateralized insurance contracts characterizes the modern regulated insurance industry. This is only possible for traditional insurance companies because of the pooling of contracts, regulation, and access to reinsurance.

A **no limit** insurance contracts technically fall under the ‘partially collateralized’ category. This contract doesn’t set a maximum coverage (i.e. the insurer is fully exposed to the total value of the item insured). Any amount of funds may be locked in multisignature escrow as collateral.

The **market object** for all insurance contracts:

"**risk**" : {
   "type" : "insurance",
   "description" : "",         **// Description of policy**
   "insurance_type" : "",      **// Full, partial, zero-limit**
   "policy_limit" : {          **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "insurance_reserve" : 0,    **// % collateral to be kept in escrow**
   "insurance_coverage" : "",  **// What the policy covers**
   "insurance_premium" : {     
      "type" : "",             **// One-off or regular**
      "schedule" : "",         **// Payment frequency**
      "bitcoin" : "",          **// Denominated in bitcoin or fiat**
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "insurance_excess" : {      **// Denominated in bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "term_days": "",            **// Term of the contract**
   "keywords": \[\]              **// Enhanced search**
}

If a claim is triggered, it may require the existing insurance contract to be replaced with a new insurance contract.

Insurance contracts could be created for several applications such as:

1.  **Dispute resolution insurance** — in the event that a Vendor loses a disputed transaction in OpenBazaar
2.  **Traditional consumer/commercial insurance **— e.g. car insurance, house insurance, health insurance
3.  **Credit default swaps** — an _insurance_ risk contract can be taken out to hedge against the risk of a _loan/bond_ defaulting.

Some of these contracts may require interaction with legacy stakeholders (i.e. the government), which will be the subject of a future article.

### Forward and Futures

Forward and futures contracts allow two parties to speculate or hedge against the price of any asset.

For example, a wheat farmer may take out a forward contract locking a sell order at a price of $100/bushel a year from now. This price would presumably guarantee the farmer to profit by an acceptable margin (provided at least X bushels are sold at that time), irrespective of whatever the actual market price is at the time.

With the forward contract, the farmer _sacrifices_ any profit that he might have gained had he risked selling at the market price a year later, **if** the market price had risen (e.g. $150/bush). Simultaneously, the forward contract_protects_ the farmer from potential losses **if** the market price decreases a year from now (e.g. $50/bushel).

Typically, neither party intend to physically purchase/sell the underlying asset. Rather, they _novate_ to settle the contract. Pure price speculation/hedging is the common purpose of forward/futures contracts.

[The unique design of forward/futures contracts in OpenBazaar is described in some detail here](https://gist.github.com/drwasho/04dbaf19da4f4a8ae512). The _updated_ **market object** schema for forward/futures contracts:

"**risk**" : {
   "type" : "forward/futures", 
   "description" : "",         **// Description of forward/future**
   "futures_asset" : "",       **// Name of the asset**
   "price\_per\_unit" : {        **// Future price; bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },   
   "limit\_per\_unit": {         **// Max up/down exposure**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "units" : "",               **// Quantity of asset** **purchased**
   "position" : "",            **// Short, long, moderator**
   "term_days": "",            **// Term of the contract**
   "oracle_source" : "",       **// Oracle user ID + sources**
   "keywords": \[\]              **// Enhanced search**
}

Under the ‘spot\_price\_source’ object, either an API source or an Oracle ID can be added to establish consensus on the tie-breaking rules governing the settlement of the contract.

### Prediction/Information

While forward and futures contract speculate and hedge against the price of an asset, **prediction markets** speculate and hedge against the future state any object or event.

For example, a prediction contract can be established between Alice and Bob based on whether it will rain the next day in Brisbane, Australia. Alice and Bob deposit 0.5 bitcoin into 2-of-3 multisignature escrow (Moderator as backup); the total value in escrow is 1 bitcoin. Alice _goes long_ (i.e. predicts rain) while Bob goes short on rain tomorrow. The next day comes and it rains; 1 bitcoin is paid out to Alice from escrow. If Bob doesn’t live in Brisbane, he may check with the Oracle (or the Weather Channel) to confirm that it did indeed rain before releasing the funds.

In this example, the chance of rain was 50%. But imagine that Alice and Bob both know that the chances of rain the next day, according to the Weather Channel, is 90%. Alice, predicting rain, deposits 0.9 bitcoin into multisignature escrow, while Bob deposits 0.1 bitcoin. As before, the winner is paid out 1 bitcoin from escrow. While ostensibly it seems that Alice is risking more than Bob, in reality her risk is lower than Bob based on the knowledge provided by the Weather Channel. In other words, the odds are overwhelmingly in Alice’s favor to collect Bob’s 0.1 bitcoin. Another way to see it is that Alice is paying a premium, in terms of risk, to entice Bob to risk his bitcoin on the outcome of an event that is unlikely to go in his favor.

There are a few key components to **prediction markets**:

1.  Selecting an appropriate _Oracle_
2.  Listing and/or discovering available prediction contracts

**_Selecting an Oracle_**

The OpenBazaar application will allow users to query the network for nodes that have identified themselves as _Oracles_, much in the same way that Moderators will be selected.

Users will be able to sort through Oracles based on reputation, category (e.g. Oracles dedicated to reporting sports games, weather, news etc), or fees. Oracles can also describe on their store-front in detail what type of reporting they perform and the sources they rely on.

![](https://cdn-images-1.medium.com/max/1200/1*jLRM0egPuDZ9qJrTdpqg2w.png)

As stated earlier, an _Oracle_ may act as either a reporting source or Moderator in a prediction contract.

**_Discovering Prediction Contracts_**

Discovery of prediction contracts is a key challenge to form an efficient prediction market.

Prediction contracts can be formed between two users on an _ad hoc_ basis, with the details negotiated directly between them. In this case, either party can create the listing contract.

Alternatively, prediction contracts could be created by _Oracles_ who commit to: 1) reporting on the state of a future event, and 2) acting as a Moderator for any prediction contracts that arise from that report. Oracles would create the contract as a Moderator, leaving open slots for a long and short position on the event. The price per share of each contract, which reflects the likelihood of the event occurring, can be dynamically updated by the _Oracle_ in real time based on their ability to match users going long or short.

OpenBazaar has a ‘follow’ feature to enable notifications, which means that a user can be notified from the _Oracle_ when new events will be reported on or new prediction contracts become available.

To minimize trust, prediction contracts can be coordinated by neutral Moderators who are not _Oracles_, who rather cite a user(s) or source as the_Oracle._

The **market object** for prediction contracts:

"**risk**" : {
   "type" : "prediction",
   "description" : "",         **// Description of prediction**
   "prediction_state" : "",    **// Future state of object/event**
   "units" : "",               **// Quantity of shares purchased**
   "price\_per\_unit" : {        **// Future price; bitcoin or fiat**
      "bitcoin" : "",
      "fiat" : {
         "price" : "",
         "currency_code" : ""
      }
   },
   "position" : "",            **// Short, long**
   "term_days": "",            **// Term of the contract**
   "oracle_source" : "",       **// Oracle user ID + sources**
   "keywords": \[\]              **// Enhanced search**
}

There are several projects attempting to create decentralized prediction markets, such as [Augur](http://www.augur.net/) and [Truthcoin](http://www.truthcoin.info/). Undoubtedly there are potential collaborative opportunities, particularly when it comes to resolving _state_ in a decentralized manner.

What is the key difference between what we hope to implement in OpenBazaar versus say Augur? The core difference is mostly philosophical: we believe that low friction markets for third party Oracles can create a supply of highly reputable _state_ reporting, at near marginal cost and at scale, over time.

While Augur is attempting to create the purest form of near-trustless state reporting (kudos to them!), we believe that markets for third party _Oracles_can solve most of the challenges associated with creating a decentralized prediction market at a fraction of the technical difficulty. High value prediction contracts may benefit from the more sophisticated and lower trust-dependent approach taken by Augur.

Deployment
----------

Implementation of risk contracts by OB1 developers is not expected until sometime next year. However, deployment may occur sooner with the help of volunteer and/or commercial contributors or partners.

That said, the existing contract schema can be tailored to include the semantic data required for most risk contracts described in this article. Moderators can also include _Oracle_-based services in their store description. As a result, we may see some early experiments in risk contracts _in lieu_ of an official implementation.

TL;DR
-----

*   OpenBazaar will enable a new user role: Oracles
*   Anyone can be an Oracle
*   Oracles can choose the level of involvement in individual transactions, from reporting to Moderating transactions
*   Risk contracts to be supported by OpenBazaar that will enable lending, insurance, forward/futures, and prediction markets

Acknowledgements
----------------

*   [Austin Williams](https://twitter.com/onewayfunction)
*   [Michael Folkson](https://twitter.com/michaelfolkson)
*   Dr Joseph Clark
*   [Dr David Strayhorn](https://www.linkedin.com/pub/david-strayhorn/2/7a9/52)
*   [Sam Patterson](https://twitter.com/SamuelPatt)
*   [Ian Grigg](https://twitter.com/iang_fc)